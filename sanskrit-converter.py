class Sanskrit99ToUnicodeConverter:
    def __init__(self):
        self.array_one = [
            "`", "ç", "ð", "¬", "ñ", "Õ", "¶", "í", "¹", "¾", "Æ", "Ó", "Ù",
            "ù", "û", "ü", "ý", "ÿ", "'", "þ", "Ÿ",
            "³", "µ", "¢", "º", "À", "¿", "†", "q+", "f+", "F+",
            "Èy", "È", "Ç", "Ô", "Ø", "Ü", "à", "ä", "æ", "è", "ì", "ï", "ö", "ô",
            "Š", "ò", "ó", "Ï", "˜", "Ý", "}", "ú", "]", "Ö", "´", "Ú", """, "Î", "Ì", "Ñ",
            "»", "¼", "Â", "Ã", "=", "•", "Å", "Ä", """, "'", "*", "'(", "D(", "H(", "q(", "Q(", "f(", "F(",
            "½", "õ", "®", "î", "(",
            "k…", "kª", "'…", "'ª", "Ê", "Ë", ")…", ")ª", "é", "ê", "÷", "ø",
            "ˆK", "ˆO", "ˆG", "ˆJ", "ˆá", "ˆk", "ˆo", "ˆg", "ˆj", "–f", "–F", "ˆ)",
            "k", "K", "Š", "o", "O", "g", "G", "¸", "\"", "'",
            "c", "C", "D", "j", "J", "H", "Á", "|",
            "q", "Q", "f", "F", "[", "{a", "{",
            "t", "T", "w", "W", "d", "x", "X", "n", "N",
            "p", "P", ")", "á", "b", "B", "É", "_", "m", "M",
            "y", "Y", "r", "+", "l", "L", "¦", "v", "V",
            "z", "Z", ";", ":", "s", "S", "h",
            "AaE", "Aae", "Aa£", "Aa", "A", "#", "$", "%", "^", "@e", "@", "\\", "§", "¤", "¥", "„",
            "ae", "aE", "a", "I", "u", "…", "‚", "U", "ª", "ƒ", "«", "¯", "&", "¨", "©", "e", "E",
            "<", "—", "~", "£", ">", "!", "œ", ",", ".", "/", "?",
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
        ]

        self.array_two = [
            "ॐ", "म्न", "श्ल", "क्ल", "श्व", "द्र्य", "ग्न", "श्च", "घ्न", "ज्ज", "त्न", "द्ब", "न्त्र",
            "हृ", "ह्न", "ह्म", "ह्य", "ह्र", "ह्ल", "ह्व", "ह्ण",
            "क्र", "ख्र", "ग्र", "घ्र", "छ्र", "ज्र", "दृ", "ट्र", "ड्र", "ढ्र",
            "त्र्य", "त्र्", "त्र", "द्र", "ध्र", "न्र", "प्र", "ब्र", "भ्र", "म्र", "व्र", "श्र", "स्र", "स्त्र",
            "क्क", "ष्ट", "ष्ठ", "द्ध", "द्घ", "प्त", "ज्ञ", "क्ष्", "क्ष", "द्व", "क्त", "न्न", "ट्ट", "द्द", "द्ग", "द्भ",
            "ङ्क", "ङ्ग", "ञ्च", "ञ्ज", "ऽ", ".", "त्त्", "त्त", "ङ्क्त", "ल्ल", "द्य", "ङ्य", "छ्य", "झ्य", "ट्य", "ठ्य", "ड्य", "ढ्य",
            "च्च", "स्न", "क्त्", "श्न", "्य",
            "कु", "कू", "ङु", "ङू", "दु", "दू", "फु", "फू", "रु", "रू", "हु", "हू",
            "क़्", "ख़्", "ग़्", "ज़्", "फ़्", "क़", "ख़", "ग़", "ज़", "ड़", "ढ़", "फ़",
            "क", "क्", "क्", "ख", "ख्", "ग", "ग्", "घ", "घ", "ङ",
            "च", "च्", "छ", "ज", "ज्", "झ", "ञ्", "ञ",
            "ट", "ठ", "ड", "ढ", "ण", "ण", "ण्",
            "त", "त्", "थ", "थ्", "द", "ध", "ध्", "न", "न्",
            "प", "प्", "फ", "फ्", "ब", "ब्", "भ", "भ्", "म", "म्",
            "य", "य्", "र", "र", "ल", "ल्", "ळ", "व", "व्",
            "श", "श्", "ष", "ष्", "स", "स्", "ह",
            "औ", "ओ", "ऑ", "आ", "अ", "इ", "ई", "उ", "ऊ", "ऐ", "ए", "ऋ", "ॠ", "ऌ", "ॡ", "कॢ",
            "ो", "ौ", "ा", "ी", "ु", "ु", "ु", "ू", "ू", "ू", "ृ", "ृ", "ृ", "ॄ", "ॄ", "े", "ै",
            "ं", "ं", "ँ", "ॅ", ":", "्", "्", "।", "॥", "॒", "॑",
            "०", "१", "२", "३", "४", "५", "६", "७", "८", "९"
        ]

        self.array_one_length = len(self.array_one)
        self.set_of_matras = "ा ॉ ि ी ु ू ृ े ै ो ौ ं : ँ ॅ"

    def replace_symbols(self, modified_substring):
        if not modified_substring:
            return modified_substring

        # Replace array_one elements with array_two elements
        for idx in range(self.array_one_length):
            modified_substring = modified_substring.replace(self.array_one[idx], self.array_two[idx])

        # Replace special glyph "¡" (reph+anusvār)
        modified_substring = modified_substring.replace("¡", "Rं")

        # Replace "i" with "ि" and correct its position
        while "i" in modified_substring:
            pos = modified_substring.find("i")
            if pos < len(modified_substring) - 1:
                char_next = modified_substring[pos + 1]
                modified_substring = modified_substring.replace(f"i{char_next}", f"{char_next}ि", 1)
            else:
                break

        # Eliminate 'chhotee ee kee maatraa' on half-letters
        while "ि्" in modified_substring:
            pos = modified_substring.find("ि्")
            if pos < len(modified_substring) - 2:
                consonant_next = modified_substring[pos + 2]
                modified_substring = modified_substring.replace(f"ि्{consonant_next}", f"्{consonant_next}ि", 1)
            else:
                break

        # Process "R" (reph) characters
        while "R" in modified_substring:
            pos_R = modified_substring.find("R")
            if pos_R <= 0:
                break

            probable_pos_hr = pos_R - 1
            while (probable_pos_hr >= 0 and 
                   modified_substring[probable_pos_hr] in self.set_of_matras):
                probable_pos_hr -= 1

            if probable_pos_hr < 0:
                break

            # Check for halant
            prev_pos = probable_pos_hr - 1
            while (prev_pos >= 0 and 
                   modified_substring[prev_pos] == "्"):
                probable_pos_hr = prev_pos - 1
                prev_pos = probable_pos_hr - 1

            if probable_pos_hr < 0:
                break

            char_to_replace = modified_substring[probable_pos_hr:pos_R]
            new_str = "र्" + char_to_replace
            modified_substring = modified_substring.replace(char_to_replace + "R", new_str, 1)

        return modified_substring

    def convert_text(self, input_text, is_html=False):
        if not is_html:
            return self.replace_symbols(input_text)
        
        # HTML processing
        processed_text = ""
        remaining_text = input_text
        
        while "Sanskrit 99" in remaining_text:
            idx = remaining_text.find("Sanskrit 99")
            idx2 = remaining_text.find(">", idx)
            idx3 = remaining_text.find("/span", idx2)
            
            if idx2 == -1 or idx3 == -1:
                break
                
            # Process nested spans
            idx4 = remaining_text.find("span", idx2)
            while idx4 < idx3:
                idx4 = remaining_text.find("span", idx3 + 4)
                idx3 = remaining_text.find("/span", idx3 + 4)
            
            modified_substring = remaining_text[idx2:idx3]
            modified_substring = self.replace_symbols(modified_substring)
            
            processed_text += remaining_text[:idx2] + modified_substring + "/span"
            remaining_text = remaining_text[idx3 + 5:]
        
        processed_text += remaining_text
        
        # Final cleanup
        processed_text = processed_text.replace("Sanskrit 99", "mangal")
        processed_text = processed_text.replace("ृलतष", "ं")
        processed_text = processed_text.replace("ृटुखतष", "घ")
        processed_text = processed_text.replace("ृामपष", "ृ")
        processed_text = processed_text.replace("ृगतष", ":")
        processed_text = processed_text.replace("ृनबसपष", "/&nbsp")
        processed_text = processed_text.replace("ाॅ", "ॉ")
        
        return processed_text

# Example usage
def main():
    converter = Sanskrit99ToUnicodeConverter()
    
    # Example with plain text
    sample_text = "k k! ki kI ku kU ke kE ko kO kM k~ ka"
    result = converter.convert_text(sample_text, is_html=False)
    print(f"Converted text: {result}")
    
    # Example with HTML
    html_text = '<span style="font-family:Sanskrit 99">k k! ki kI ku kU ke kE ko kO kM k~ ka</span>'
    result_html = converter.convert_text(html_text, is_html=True)
    print(f"Converted HTML: {result_html}")

if __name__ == "__main__":
    main()
