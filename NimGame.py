class NimGame(object):
    def canWinNim(self, n):
        if n < 0 or n % 4 == 0:
            return False
        return True