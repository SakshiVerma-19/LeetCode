class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # Position to write compressed characters
        read = 0   # Position to read characters

        while read < len(chars):
            char = chars[read]
            count = 0

            
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            # Write the character
            chars[write] = char
            write += 1

            # Write the count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write

            