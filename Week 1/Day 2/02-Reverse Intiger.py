def reverse(self, x: int) -> int:
        if x < 0:
            x = x.strip("-")
            x = str(x)
            return("-" + str(x[::-1]))
        x = str(x)
        
        return(x[::-1])