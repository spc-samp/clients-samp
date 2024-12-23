using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Xml.Linq;

namespace Client_R5_SPC.Services
{
    public class Language
    {
        private Dictionary<string, string> Translation_Dictionary = new();
        private List<string> Available_Languages;

        public List<string> GetAvailable_Languages()
        {
            var Current_Assembly = Assembly.GetExecutingAssembly();
            Available_Languages = Current_Assembly.GetManifestResourceNames().Where(Resource => Resource.Contains("translations") && Resource.EndsWith(".xml"))
                .Select(Resource => Path.GetFileNameWithoutExtension(Resource.Split('.').ElementAt(Resource.Split('.').Length - 2))).ToList();

            return Available_Languages;
        }

        public void Load_Translations(string Language_Name)
        {
            var Current_Assembly = Assembly.GetExecutingAssembly();
            string Resource_Name = Current_Assembly.GetManifestResourceNames().FirstOrDefault(Resource => Resource.Contains("translations") && Resource.EndsWith($"{Language_Name}.xml"));

            if (string.IsNullOrEmpty(Resource_Name))
                throw new Exception($"Error: No translation resources found for '{Language_Name}'");

            Translation_Dictionary.Clear();
            using var Resource_Stream = Current_Assembly.GetManifestResourceStream(Resource_Name);
            var XML_Document = XDocument.Load(Resource_Stream);

            Translation_Dictionary = XML_Document.Descendants("string").ToDictionary(Element => Element.Attribute("key")?.Value ?? string.Empty, Element => Element.Value);
        }

        public string Translate(string Key) => 
            Translation_Dictionary.TryGetValue(Key, out var Value) ? Value : Key;
    }
}