using System;
using System.Collections.Generic;
using System.IO;

namespace Client_R3_Voip_SPC.Services
{
    public interface Language_Mapping_II
    {
        string GetImage_Code(string Language_Name);
        void Add_Mapping(string Language_Name, string Image_Code);
        bool Has_Mapping(string Language_Name);
    }

    public class Language_Mapping : Language_Mapping_II
    {
        private readonly Dictionary<string, string> LanguageTo_ImageCode;

        public Language_Mapping()
        {
            LanguageTo_ImageCode = new Dictionary<string, string>
            {
                { "Bahasa Indonesia", "id" },
                { "Български", "bg" },
                { "Čeština", "cs" },
                { "Dansk", "da" },
                { "Deutsch", "de" },
                { "Ελληνικά", "el" },
                { "English", "en" },
                { "Español", "es" },
                { "Français", "fr" },
                { "हिन्दी", "hi" },
                { "Hrvatski", "hr" },
                { "Italiano", "it" },
                { "日本語", "ja" },
                { "한국어", "ko" },
                { "Magyar", "hu" },
                { "Nederlands", "nl" },
                { "Norsk", "no" },
                { "Polski", "pl" },
                { "Português", "pt" },
                { "Română", "ro" },
                { "Русский", "ru" },
                { "Српски", "sr" },
                { "Suomi", "fi" },
                { "Svenska", "sv" },
                { "ไทย", "th" },
                { "Tiếng Việt", "vi" },
                { "Türk", "tr" },
                { "Українська", "uk" },
                { "العربية", "ar" },
                { "中文", "zh" }
            };
        }

        public string GetImage_Code(string Language_Name)
        {
            Language_Name = Path.GetFileNameWithoutExtension(Language_Name);
            return LanguageTo_ImageCode.TryGetValue(Language_Name, out var Code) ? Code : Language_Name.ToLower();
        }

        public void Add_Mapping(string Language_Name, string Image_Code)
        {
            if (string.IsNullOrWhiteSpace(Language_Name) || string.IsNullOrWhiteSpace(Image_Code))
                throw new ArgumentException("Error: Language name and image code cannot be empty.");

            LanguageTo_ImageCode[Language_Name] = Image_Code;
        }

        public bool Has_Mapping(string Language_Name) =>
            LanguageTo_ImageCode.ContainsKey(Path.GetFileNameWithoutExtension(Language_Name));
    }
}