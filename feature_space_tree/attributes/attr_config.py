from attr import *

class EnumTermLex(object):
    (REG_EXP,
     N_GRAM_CHAR,
     LOCAL_N_GRAM_CHAR,
     LOCAL_REGEXP,
     BIGRAM,
     TRIGRAM,
     BIGRAM_STYLE_POS,
     TRIGRAM_STYLE_POS,
     N_GRAM_TOKEN,
     BIGRAM_COLLOCATION,
     TRIGRAM_COLLOCATION,
     TOKEN_LEN,
     SENT_LEN,
     SENT_STOPS_LEN,
     SENT_NO_STOPS_LEN,
     BIGRAM_STOPS,
     TRIGRAM_STOPS,
     BIGRAM_STOPS_COLLOCATION,
     TRIGRAM_STOPS_COLLOCATION,
     BIGRAM_STOPSPUNTC_COLLOCATION,
     TRIGRAM_STOPSPUNTC_COLLOCATION,
     POS,
     MERGED,
     AMBIGUOUS,
     SPLIT,
     REG_EXP_IGNORE) = range(26)
     

class FactoryTerm(object):

    __metaclass__ = ABCMeta

    def build_tokens(self, option, kwargs_term):
        option = eval(option)
        return self.create(option, kwargs_term)

    @abstractmethod
    def create(self, option, kwargs):
        pass

# FIXME: It wouldbe a good thing to normalize the convention to name each 
# inherited class This is because sometimes I use the super class as a sufix, 
# and other times as a prefix.

# FIXME: I don't like this constructions, all Terms receives the object kwargs
# and each class process it. This gives to each Term class a second 
# resposability (process the kawargs). This preprocessing could be done in the 
# Factory, in this way we delegate ALL the resposability to the factory.

class FactoryTermLex(FactoryTerm):

    def create(self, option, kwargs):

        if option == EnumTermLex.REG_EXP:
            # !!! DEBUG: print "KWARGS: " + str(kwargs)
            return TermRegExp(kwargs)
        if option == EnumTermLex.SPLIT:
            return TermSplit(kwargs)

        elif option == EnumTermLex.N_GRAM_CHAR:
            return TermNGramChar(kwargs)

        elif option == EnumTermLex.LOCAL_N_GRAM_CHAR:
            return TermLocalNGramChar(kwargs)

        elif option == EnumTermLex.BIGRAM:
            return TermBigram(kwargs)

        elif option == EnumTermLex.TRIGRAM:
            return TermTrigram(kwargs)
        elif option == EnumTermLex.BIGRAM_STYLE_POS:
            return TermBigramStylePOS(kwargs)

        elif option == EnumTermLex.TRIGRAM_STYLE_POS:
            return TermTrigramStylePOS(kwargs)

        elif option == EnumTermLex.N_GRAM_TOKEN:
            return TermNGramToken(kwargs)

        elif option == EnumTermLex.BIGRAM_COLLOCATION:
            return TermBigramCollocation(kwargs)

        elif option == EnumTermLex.TRIGRAM_COLLOCATION:
            return TermTrigramCollocation(kwargs)

        elif option == EnumTermLex.TOKEN_LEN:
            return TermTokenLenght(kwargs)

        elif option == EnumTermLex.SENT_LEN:
            return TermSentLenght(kwargs)

        elif option == EnumTermLex.SENT_STOPS_LEN:
            return TermSentStopsLenght(kwargs)

        elif option == EnumTermLex.SENT_NO_STOPS_LEN:
            return TermSentNOStopsLenght(kwargs)
        
        elif option == EnumTermLex.BIGRAM_STOPS:
            return TermBigramStop(kwargs)
        
        elif option == EnumTermLex.TRIGRAM_STOPS:
            return TermTrigramStop(kwargs)

        elif option == EnumTermLex.BIGRAM_STOPS_COLLOCATION:
            return TermBigramCollocationStop(kwargs)
        
        elif option == EnumTermLex.TRIGRAM_STOPS_COLLOCATION:
            return TermTrigramCollocationStop(kwargs)
        
        elif option == EnumTermLex.BIGRAM_STOPSPUNTC_COLLOCATION:
            return TermBigramCollocationStopPuntc(kwargs)
        
        elif option == EnumTermLex.TRIGRAM_STOPSPUNTC_COLLOCATION:
            return TermTrigramCollocationStopPuntc(kwargs)
        
        elif option == EnumTermLex.POS:
            return TermPOS(kwargs)
        
        elif option == EnumTermLex.AMBIGUOUS:
            return TermAmbiguousWords(kwargs)

        elif option == EnumTermLex.REG_EXP_IGNORE:
            return TermRegExpIgnore(kwargs)
        
        elif option == EnumTermLex.LOCAL_REGEXP:
            return TermLocalRegExp(kwargs)

        #elif option == EnumTermLex.SFM:
        #    return TermSFM(kwargs[0])

        elif option == EnumTermLex.MERGED:
            tokens = Util.get_merged_tokens(kwargs)

            #tokens = (Tokens(kwargs, TermPuntc()).tokens +
            #          Tokens(kwargs, TermWordLenght()).tokens +
            #        Tokens(kwargs, TermSentLenght()).tokens +
            #        Tokens(kwargs, TermSentStopsLenght()).tokens +
            #        Tokens(kwargs, TermSentNOStopsLenght()).tokens +
            #        Tokens(kwargs, TermSentPuntcLenght()).tokens +
            #        Tokens(kwargs, TermBigramCollocation()).tokens +
            #        Tokens(kwargs, TermTrigramCollocation()).tokens #+
                    #Tokens(kwargs, TermRegExp()).tokens
                    #Tokens(kwargs, TermBigramCollocationStop()).tokens +
                    #Tokens(kwargs, TermTrigramCollocationStop()).tokens
            #        )
            # print "THE TOKENS: " + str(tokens)
            return Merged(tokens)