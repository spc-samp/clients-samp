using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Windows.Forms;
using System.ComponentModel;
using System.Drawing.Text;
using System.Threading;
using Client_R4_SPC.Models;

namespace Client_R4_SPC.UI
{
    [DefaultProperty("Value")]
    public class Custom_ProgressBar : ProgressBar
    {
        private int Animation_Step = 0;
        private System.Windows.Forms.Timer Animation_Timer;
        private float Current_Value = 0;
        private bool Is_Animating = false;
        private int Custom_Value;
        private bool Is_Completed = false;
        private System.Windows.Forms.Timer Completion_Timer;
        private string Progress_Text = "";

        private Color GradientStart_Color_II;
        private Color GradientEnd_Color_II;
        private Color Background_Color_II;
        private int Animation_Speed_II = 10;
        private int Corner_Radius_II = 5;
        private bool Show_Percentage_II = true;
        
        public Custom_ProgressBar()
        {
            SetStyle(ControlStyles.UserPaint | ControlStyles.AllPaintingInWmPaint | ControlStyles.OptimizedDoubleBuffer, true);
            
            Animation_Timer = new System.Windows.Forms.Timer();
            Animation_Timer.Interval = 1;
            Animation_Timer.Tick += AnimationTimer_Tick;

            Completion_Timer = new System.Windows.Forms.Timer();
            Completion_Timer.Tick += CompletionTimer_Tick;
            Completion_Timer.Interval = 4*500;

            GradientStart_Color_II = Colors_Client.Accent;
            GradientEnd_Color_II = Color.FromArgb(Colors_Client.Accent.R + 20, Colors_Client.Accent.G + 20, Colors_Client.Accent.B + 20);
            Background_Color_II = Colors_Client.Secondary;
        }

        private void CompletionTimer_Tick(object sender, EventArgs e)
        {
            Completion_Timer.Stop();
            OnCompletion?.Invoke(this, EventArgs.Empty);
        }

        public event EventHandler OnCompletion;

        [Category("Aparência")]
        [DefaultValue(typeof(Color), "0, 139, 139")]
        [Description("Cor inicial do gradiente da barra de progresso")]
        public Color GradientStart_Color
        {
            get => GradientStart_Color_II;
            set
            {
                GradientStart_Color_II = value;
                Invalidate();
            }
        }

        [Category("Aparência")]
        [DefaultValue(typeof(Color), "20, 159, 159")]
        [Description("Cor final do gradiente da barra de progresso")]
        public Color GradientEnd_Color
        {
            get => GradientEnd_Color_II;
            set
            {
                GradientEnd_Color_II = value;
                Invalidate();
            }
        }

        [Category("Aparência")]
        [DefaultValue(typeof(Color), "47, 49, 54")]
        [Description("Cor de fundo da barra de progresso")]
        public Color Background_Color
        {
            get => Background_Color_II;
            set
            {
                Background_Color_II = value;
                Invalidate();
            }
        }

        [Category("Animação")]
        [DefaultValue(10)]
        [Description("Velocidade da animação (quanto menor, mais rápido)")]
        public int Animation_Speed
        {
            get => Animation_Speed_II;
            set
            {
                Animation_Speed_II = Math.Max(1, Math.Min(value, 100));
                Invalidate();
            }
        }

        [Category("Aparência")]
        [DefaultValue(5)]
        [Description("Raio dos cantos arredondados")]
        public int Corner_Radius
        {
            get => Corner_Radius_II;
            set
            {
                Corner_Radius_II = Math.Max(0, Math.Min(value, 15));
                Invalidate();
            }
        }

        [Category("Aparência")]
        [DefaultValue(true)]
        [Description("Mostra ou oculta o texto de porcentagem")]
        public bool Show_Percentage
        {
            get => Show_Percentage_II;
            set
            {
                Show_Percentage_II = value;
                Invalidate();
            }
        }

        [Browsable(true)]
        [Category("Comportamento")]
        [Description("Valor atual da barra de progresso")]
        [DefaultValue(0)]
        public new int Value
        {
            get { return Custom_Value; }
            set 
            { 
                if (value != Custom_Value)
                {
                    Custom_Value = Math.Max(Minimum, Math.Min(value, Maximum));
                    base.Value = Custom_Value;
                    
                    if (Custom_Value >= Maximum && !Is_Completed)
                    {
                        Progress_Text = "100%";
                        Is_Completed = true;
                        
                        var CompletionDelay_Timer = new System.Windows.Forms.Timer();
                        CompletionDelay_Timer.Interval = 3*500;
                        CompletionDelay_Timer.Tick += (s, e) =>
                        {
                            Progress_Text = "Completed...";
                            CompletionDelay_Timer.Stop();
                            CompletionDelay_Timer.Dispose();
                            
                            Completion_Timer.Start();
                        };
                        CompletionDelay_Timer.Start();
                    }
                    else if (Custom_Value < Maximum)
                    {
                        Is_Completed = false;
                        Progress_Text = "";
                    }
                    
                    Start_Animation();
                    this.Refresh();
                }
            }
        }

        private void Start_Animation()
        {
            if (!Is_Animating)
            {
                Current_Value = Custom_Value;
                Is_Animating = true;
                Animation_Timer.Start();
            }
        }

        private void AnimationTimer_Tick(object sender, EventArgs e)
        {
            float Target_Value = Custom_Value;
            float Step = (Target_Value - Current_Value) / Animation_Speed_II;

            if (Math.Abs(Target_Value - Current_Value) < 0.1)
            {
                Current_Value = Target_Value;
                Is_Animating = false;
                Animation_Timer.Stop();
            }
            else
                Current_Value += Step;

            Animation_Step = (Animation_Step + 1) % 360;
            Invalidate();
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.TextRenderingHint = TextRenderingHint.ClearTypeGridFit;

            Rectangle Rect = ClientRectangle;
            
            using (var Path = GetRounded_Rectangle(Rect, Corner_Radius_II))
            using (var Brush = new SolidBrush(Background_Color_II))
            {
                e.Graphics.FillPath(Brush, Path);
            }

            int Progress_Width = (int)(Rect.Width * (Current_Value / Maximum));
            
            if (Progress_Width > 0)
            {
                Rectangle Progress_Rect = new Rectangle(Rect.X, Rect.Y, Progress_Width, Rect.Height);

                using (var Path = GetRounded_Rectangle(Progress_Rect, Corner_Radius_II))
                using (var Gradient = new LinearGradientBrush(Progress_Rect, GradientStart_Color_II, GradientEnd_Color_II, LinearGradientMode.Horizontal))
                {
                    float[] Positions = { 0.0f, 0.5f, 1.0f };
                    Color[] Colors = {GradientStart_Color_II,  Color.FromArgb(255, Math.Min(GradientStart_Color_II.R + 30, 255), Math.Min(GradientStart_Color_II.G + 30, 255), Math.Min(GradientStart_Color_II.B + 30, 255)), GradientEnd_Color_II};

                    ColorBlend Blend = new ColorBlend();
                    Blend.Positions = Positions;
                    Blend.Colors = Colors;
                    Gradient.InterpolationColors = Blend;

                    Matrix Matrix = new Matrix();
                    Matrix.RotateAt(Animation_Step, new PointF(Progress_Rect.Left + Progress_Rect.Width / 2, Progress_Rect.Top + Progress_Rect.Height / 2));
                    Gradient.MultiplyTransform(Matrix);

                    e.Graphics.FillPath(Gradient, Path);
                }

                using (var Path = GetRounded_Rectangle(Progress_Rect, Corner_Radius_II))
                using (var Pen = new Pen(Color.FromArgb(50, Color.White), 1))
                {
                    e.Graphics.DrawPath(Pen, Path);
                }
            }

            if (Show_Percentage_II)
            {
                string displayString = Is_Completed ? Progress_Text : $"{(int)((Current_Value / Maximum) * 100)}%";
                using (var font = new Font("Segoe UI", 8.25f, FontStyle.Bold))
                {
                    SizeF textSize = e.Graphics.MeasureString(displayString, font);
                    PointF textPos = new PointF((Rect.Width - textSize.Width) / 2, (Rect.Height - textSize.Height) / 2);

                    using (var brush = new SolidBrush(Color.FromArgb(50, Color.Black)))
                    {
                        e.Graphics.DrawString(displayString, font, brush, new PointF(textPos.X + 1, textPos.Y + 1));
                    }

                    using (var brush = new SolidBrush(Colors_Client.Text))
                    {
                        e.Graphics.DrawString(displayString, font, brush, textPos);
                    }
                }
            }
        }
        
        private GraphicsPath GetRounded_Rectangle(Rectangle rect, int radius)
        {
            GraphicsPath Path = new GraphicsPath();
            int Diameter = radius * 2;

            Path.AddArc(rect.X, rect.Y, Diameter, Diameter, 180, 90);
            Path.AddArc(rect.Width - Diameter + rect.X, rect.Y, Diameter, Diameter, 270, 90); 
            Path.AddArc(rect.Width - Diameter + rect.X, rect.Height - Diameter + rect.Y, Diameter, Diameter, 0, 90);
            Path.AddArc(rect.X, rect.Height - Diameter + rect.Y, Diameter, Diameter, 90, 90);

            Path.CloseFigure();
            return Path;
        }
    }
}