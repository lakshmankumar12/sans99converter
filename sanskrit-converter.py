import re

class Sanskrit99ToUnicode:
    def __init__(self):
        # Basic character mappings
        self.char_map = {
            'A': '\u0905',    # अ
            'a': '',          # Inherent 'a' sound
            'š': '\u093E',    # ा
            'i': '\u093F',    # ि
            'I': '\u0908',    # ई
            'u': '\u0941',    # ु
            'U': '\u0942',    # ू
            '†': '\u0943',    # ृ
            'e': '\u0947',    # े
            'E': '\u0948',    # ै
            'ae': '\u0948',   # ै
            'o': '\u094B',    # ो
            'O': '\u094C',    # ौ
            '<': '\u0919',    # ङ
            'p': '\u092A',    # प
            'g': '\u0917',    # ग
            'œ': '\u094D',    # ्
            'r': '\u0930',    # र
            '[': '\u0921',    # ड
            '\'': '\u093D',   # ऽ
            'y': '\u092F',    # य
            'v': '\u0935',    # व
            'h': '\u0939',    # ह
            'm': '\u092E',    # म
            '‚': '\u0902',    # ं
            '/': '',          # Ignore
            'w': '\u0924',    # त
            'n': '\u0928',    # न
            'j': '\u091C',    # ज
            'b': '\u092C',    # ब
            'c': '\u091A',    # च
            'l': '\u0932',    # ल
            's': '\u0938',    # स
            'k': '\u0915',    # क
            'd': '\u0926',    # द
            'x': '\u0915\u094D\u0937',  # क्ष
            'D': '\u0927',    # ध
            'N': '\u0923',    # ण
            'B': '\u092D',    # भ
            # Add more mappings as needed
        }

        # Special combinations and conjuncts
        self.special_combinations = {
            'š/': '\u093E',   # ा
            '‚/': '\u0902',   # ं
            'œ/': '\u094D',   # ्
        }

    def convert(self, text):
        result = ''
        i = 0
        while i < len(text):
            # Check for special combinations first
            found_special = False
            for combo in self.special_combinations:
                if text[i:].startswith(combo):
                    result += self.special_combinations[combo]
                    i += len(combo)
                    found_special = True
                    break
            
            if found_special:
                continue

            # Handle regular characters
            if text[i] in self.char_map:
                result += self.char_map[text[i]]
            else:
                result += text[i]  # Keep unchanged if no mapping exists
            i += 1

        # Post-processing
        result = self._post_process(result)
        return result

    def _post_process(self, text):
        # Handle specific post-processing rules
        # For example, rearranging vowel marks
        text = re.sub(r'([^\u0900-\u097F])(\u093E|\u093F|\u0940)', r'\2\1', text)
        return text

# Example usage
def main():
    converter = Sanskrit99ToUnicode()
    
    # Test with your sample text
    sample = "Aw p<cag<éÔa[a< NyaspUvRk< jphaemacRnai-;ek ivix< vyašrVyaSya/m>"
    converted = converter.convert(sample)
    print("Original:", sample)
    print("Converted:", converted)

if __name__ == "__main__":
    main()
