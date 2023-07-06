import jamspell

corrector = jamspell.TSpellCorrector()
corrector.LoadLangModel('en.bin')

def fix_fragment(fragment: str) -> str:
    # corrected = corrector.FixFragment(fragment)
    # return corrected
    pass

if __name__ == "__main__":
    
    print(corrector.FixFragment('I am the begt spell cherken!'))
    # u'I am the best spell checker!'
    print(corrector.GetCandidates(['i', 'am', 'the', 'begt', 'spell', 'cherken'], 3))
    # (u'best', u'beat', u'belt', u'bet', u'bent', ... )
    print(corrector.GetCandidates(['i', 'am', 'the', 'begt', 'spell', 'cherken'], 5))
    # (u'checker', u'chicken', u'checked', u'wherein', u'coherent', ...)