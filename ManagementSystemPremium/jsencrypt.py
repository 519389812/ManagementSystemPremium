__all__ = ['jsencrypt']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([])
@Js
def PyJs_anonymous_0_(exports, this, arguments, var=var):
    var = Scope({'exports':exports, 'this':this, 'arguments':arguments}, var)
    var.registers(['b64map', 'op_xor', '__extends', 'parseBigInt', 'onMouseMoveListener_1', 'am1', 'pkcs1pad2', 'Stream', 'Int10', 'rng_pptr', 'intAt', 'Hex', 'JSEncrypt', 'BI_FP', 'DIGEST_HEADERS', 'YAHOO', 'ASN1Tag', 'am3', 'rr', 'Arcfour', 'nbi', 'nbv', 'rng_state', 'RSAKey', 'getDigestHeader', 'lbit', 'Base64', 'BI_RM', 'nbits', 'SecureRandom', 'cbit', 'dbits', 'am2', 'reTimeL', 'decoder', 'KJUR', 'JSEncryptRSAKey', 'NullExp', 'lowprimes', 'j_lm', 'stringCut', 'BI_RC', 'pkcs1unpad2', 'ellipsis', 'rng_psize', 'vv', 'canary', 't', 'reTimeS', 'prng_newstate', 'z', 'removeDigestHeader', 'hex2b64', 'op_andnot', 'BigInteger', 'Montgomery', 'b64pad', 'op_or', 'max', 'Classic', 'rng_pool', 'decoder$1', 'b64tohex', 'Barrett', 'int2char', 'pkcs1pad1', 'exports', 'lplim', 'ASN1', 'op_and', 'rng_get_byte', 'extendStatics'])
    @Js
    def PyJsHoisted_int2char_(n, this, arguments, var=var):
        var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['n'])
        return var.get('BI_RM').callprop('charAt', var.get('n'))
    PyJsHoisted_int2char_.func_name = 'int2char'
    var.put('int2char', PyJsHoisted_int2char_)
    @Js
    def PyJsHoisted_op_and_(x, y, this, arguments, var=var):
        var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
        var.registers(['y', 'x'])
        return (var.get('x')&var.get('y'))
    PyJsHoisted_op_and_.func_name = 'op_and'
    var.put('op_and', PyJsHoisted_op_and_)
    @Js
    def PyJsHoisted_op_or_(x, y, this, arguments, var=var):
        var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
        var.registers(['y', 'x'])
        return (var.get('x')|var.get('y'))
    PyJsHoisted_op_or_.func_name = 'op_or'
    var.put('op_or', PyJsHoisted_op_or_)
    @Js
    def PyJsHoisted_op_xor_(x, y, this, arguments, var=var):
        var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
        var.registers(['y', 'x'])
        return (var.get('x')^var.get('y'))
    PyJsHoisted_op_xor_.func_name = 'op_xor'
    var.put('op_xor', PyJsHoisted_op_xor_)
    @Js
    def PyJsHoisted_op_andnot_(x, y, this, arguments, var=var):
        var = Scope({'x':x, 'y':y, 'this':this, 'arguments':arguments}, var)
        var.registers(['y', 'x'])
        return (var.get('x')&(~var.get('y')))
    PyJsHoisted_op_andnot_.func_name = 'op_andnot'
    var.put('op_andnot', PyJsHoisted_op_andnot_)
    @Js
    def PyJsHoisted_lbit_(x, this, arguments, var=var):
        var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
        var.registers(['x', 'r'])
        if (var.get('x')==Js(0.0)):
            return (-Js(1.0))
        var.put('r', Js(0.0))
        if ((var.get('x')&Js(65535))==Js(0.0)):
            var.put('x', Js(16.0), '>>')
            var.put('r', Js(16.0), '+')
        if ((var.get('x')&Js(255))==Js(0.0)):
            var.put('x', Js(8.0), '>>')
            var.put('r', Js(8.0), '+')
        if ((var.get('x')&Js(15))==Js(0.0)):
            var.put('x', Js(4.0), '>>')
            var.put('r', Js(4.0), '+')
        if ((var.get('x')&Js(3.0))==Js(0.0)):
            var.put('x', Js(2.0), '>>')
            var.put('r', Js(2.0), '+')
        if ((var.get('x')&Js(1.0))==Js(0.0)):
            var.put('r',Js(var.get('r').to_number())+Js(1))
        return var.get('r')
    PyJsHoisted_lbit_.func_name = 'lbit'
    var.put('lbit', PyJsHoisted_lbit_)
    @Js
    def PyJsHoisted_cbit_(x, this, arguments, var=var):
        var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
        var.registers(['x', 'r'])
        var.put('r', Js(0.0))
        while (var.get('x')!=Js(0.0)):
            var.put('x', (var.get('x')-Js(1.0)), '&')
            var.put('r',Js(var.get('r').to_number())+Js(1))
        return var.get('r')
    PyJsHoisted_cbit_.func_name = 'cbit'
    var.put('cbit', PyJsHoisted_cbit_)
    @Js
    def PyJsHoisted_hex2b64_(h, this, arguments, var=var):
        var = Scope({'h':h, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'ret', 'h', 'c'])
        pass
        pass
        var.put('ret', Js(''))
        #for JS loop
        var.put('i', Js(0.0))
        while ((var.get('i')+Js(3.0))<=var.get('h').get('length')):
            try:
                var.put('c', var.get('parseInt')(var.get('h').callprop('substring', var.get('i'), (var.get('i')+Js(3.0))), Js(16.0)))
                var.put('ret', (var.get('b64map').callprop('charAt', (var.get('c')>>Js(6.0)))+var.get('b64map').callprop('charAt', (var.get('c')&Js(63.0)))), '+')
            finally:
                    var.put('i', Js(3.0), '+')
        if ((var.get('i')+Js(1.0))==var.get('h').get('length')):
            var.put('c', var.get('parseInt')(var.get('h').callprop('substring', var.get('i'), (var.get('i')+Js(1.0))), Js(16.0)))
            var.put('ret', var.get('b64map').callprop('charAt', (var.get('c')<<Js(2.0))), '+')
        else:
            if ((var.get('i')+Js(2.0))==var.get('h').get('length')):
                var.put('c', var.get('parseInt')(var.get('h').callprop('substring', var.get('i'), (var.get('i')+Js(2.0))), Js(16.0)))
                var.put('ret', (var.get('b64map').callprop('charAt', (var.get('c')>>Js(2.0)))+var.get('b64map').callprop('charAt', ((var.get('c')&Js(3.0))<<Js(4.0)))), '+')
        while ((var.get('ret').get('length')&Js(3.0))>Js(0.0)):
            var.put('ret', var.get('b64pad'), '+')
        return var.get('ret')
    PyJsHoisted_hex2b64_.func_name = 'hex2b64'
    var.put('hex2b64', PyJsHoisted_hex2b64_)
    @Js
    def PyJsHoisted_b64tohex_(s, this, arguments, var=var):
        var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['k', 'ret', 'v', 'slop', 'i', 's'])
        var.put('ret', Js(''))
        pass
        var.put('k', Js(0.0))
        var.put('slop', Js(0.0))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('s').get('length')):
            try:
                if (var.get('s').callprop('charAt', var.get('i'))==var.get('b64pad')):
                    break
                var.put('v', var.get('b64map').callprop('indexOf', var.get('s').callprop('charAt', var.get('i'))))
                if (var.get('v')<Js(0.0)):
                    continue
                if (var.get('k')==Js(0.0)):
                    var.put('ret', var.get('int2char')((var.get('v')>>Js(2.0))), '+')
                    var.put('slop', (var.get('v')&Js(3.0)))
                    var.put('k', Js(1.0))
                else:
                    if (var.get('k')==Js(1.0)):
                        var.put('ret', var.get('int2char')(((var.get('slop')<<Js(2.0))|(var.get('v')>>Js(4.0)))), '+')
                        var.put('slop', (var.get('v')&Js(15)))
                        var.put('k', Js(2.0))
                    else:
                        if (var.get('k')==Js(2.0)):
                            var.put('ret', var.get('int2char')(var.get('slop')), '+')
                            var.put('ret', var.get('int2char')((var.get('v')>>Js(2.0))), '+')
                            var.put('slop', (var.get('v')&Js(3.0)))
                            var.put('k', Js(3.0))
                        else:
                            var.put('ret', var.get('int2char')(((var.get('slop')<<Js(2.0))|(var.get('v')>>Js(4.0)))), '+')
                            var.put('ret', var.get('int2char')((var.get('v')&Js(15))), '+')
                            var.put('k', Js(0.0))
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
        if (var.get('k')==Js(1.0)):
            var.put('ret', var.get('int2char')((var.get('slop')<<Js(2.0))), '+')
        return var.get('ret')
    PyJsHoisted_b64tohex_.func_name = 'b64tohex'
    var.put('b64tohex', PyJsHoisted_b64tohex_)
    @Js
    def PyJsHoisted___extends_(d, b, this, arguments, var=var):
        var = Scope({'d':d, 'b':b, 'this':this, 'arguments':arguments}, var)
        var.registers(['__', 'b', 'd'])
        @Js
        def PyJsHoisted____(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            var.get(u"this").put('constructor', var.get('d'))
        PyJsHoisted____.func_name = '__'
        var.put('__', PyJsHoisted____)
        var.get('extendStatics')(var.get('d'), var.get('b'))
        pass
        var.get('d').put('prototype', (var.get('Object').callprop('create', var.get('b')) if PyJsStrictEq(var.get('b'),var.get(u"null")) else PyJsComma(var.get('__').put('prototype', var.get('b').get('prototype')),var.get('__').create())))
    PyJsHoisted___extends_.func_name = '__extends'
    var.put('__extends', PyJsHoisted___extends_)
    @Js
    def PyJsHoisted_stringCut_(str, len, this, arguments, var=var):
        var = Scope({'str':str, 'len':len, 'this':this, 'arguments':arguments}, var)
        var.registers(['str', 'len'])
        if (var.get('str').get('length')>var.get('len')):
            var.put('str', (var.get('str').callprop('substring', Js(0.0), var.get('len'))+var.get('ellipsis')))
        return var.get('str')
    PyJsHoisted_stringCut_.func_name = 'stringCut'
    var.put('stringCut', PyJsHoisted_stringCut_)
    @Js
    def PyJsHoisted_nbi_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        return var.get('BigInteger').create(var.get(u"null"))
    PyJsHoisted_nbi_.func_name = 'nbi'
    var.put('nbi', PyJsHoisted_nbi_)
    @Js
    def PyJsHoisted_parseBigInt_(str, r, this, arguments, var=var):
        var = Scope({'str':str, 'r':r, 'this':this, 'arguments':arguments}, var)
        var.registers(['r', 'str'])
        return var.get('BigInteger').create(var.get('str'), var.get('r'))
    PyJsHoisted_parseBigInt_.func_name = 'parseBigInt'
    var.put('parseBigInt', PyJsHoisted_parseBigInt_)
    @Js
    def PyJsHoisted_am1_(i, x, w, j, c, n, this, arguments, var=var):
        var = Scope({'i':i, 'x':x, 'w':w, 'j':j, 'c':c, 'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['x', 'w', 'c', 'v', 'i', 'j', 'n'])
        while (var.put('n',Js(var.get('n').to_number())-Js(1))>=Js(0.0)):
            var.put('v', (((var.get('x')*var.get(u"this").get((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))))+var.get('w').get(var.get('j')))+var.get('c')))
            var.put('c', var.get('Math').callprop('floor', (var.get('v')/Js(67108864))))
            var.get('w').put((var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1)), (var.get('v')&Js(67108863)))
        return var.get('c')
    PyJsHoisted_am1_.func_name = 'am1'
    var.put('am1', PyJsHoisted_am1_)
    @Js
    def PyJsHoisted_am2_(i, x, w, j, c, n, this, arguments, var=var):
        var = Scope({'i':i, 'x':x, 'w':w, 'j':j, 'c':c, 'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['x', 'w', 'm', 'xh', 'c', 'i', 'xl', 'l', 'j', 'n', 'h'])
        var.put('xl', (var.get('x')&Js(32767)))
        var.put('xh', (var.get('x')>>Js(15.0)))
        while (var.put('n',Js(var.get('n').to_number())-Js(1))>=Js(0.0)):
            var.put('l', (var.get(u"this").get(var.get('i'))&Js(32767)))
            var.put('h', (var.get(u"this").get((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)))>>Js(15.0)))
            var.put('m', ((var.get('xh')*var.get('l'))+(var.get('h')*var.get('xl'))))
            var.put('l', ((((var.get('xl')*var.get('l'))+((var.get('m')&Js(32767))<<Js(15.0)))+var.get('w').get(var.get('j')))+(var.get('c')&Js(1073741823))))
            var.put('c', (((PyJsBshift(var.get('l'),Js(30.0))+PyJsBshift(var.get('m'),Js(15.0)))+(var.get('xh')*var.get('h')))+PyJsBshift(var.get('c'),Js(30.0))))
            var.get('w').put((var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1)), (var.get('l')&Js(1073741823)))
        return var.get('c')
    PyJsHoisted_am2_.func_name = 'am2'
    var.put('am2', PyJsHoisted_am2_)
    @Js
    def PyJsHoisted_am3_(i, x, w, j, c, n, this, arguments, var=var):
        var = Scope({'i':i, 'x':x, 'w':w, 'j':j, 'c':c, 'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['x', 'w', 'm', 'xh', 'c', 'i', 'xl', 'l', 'j', 'n', 'h'])
        var.put('xl', (var.get('x')&Js(16383)))
        var.put('xh', (var.get('x')>>Js(14.0)))
        while (var.put('n',Js(var.get('n').to_number())-Js(1))>=Js(0.0)):
            var.put('l', (var.get(u"this").get(var.get('i'))&Js(16383)))
            var.put('h', (var.get(u"this").get((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)))>>Js(14.0)))
            var.put('m', ((var.get('xh')*var.get('l'))+(var.get('h')*var.get('xl'))))
            var.put('l', ((((var.get('xl')*var.get('l'))+((var.get('m')&Js(16383))<<Js(14.0)))+var.get('w').get(var.get('j')))+var.get('c')))
            var.put('c', (((var.get('l')>>Js(28.0))+(var.get('m')>>Js(14.0)))+(var.get('xh')*var.get('h'))))
            var.get('w').put((var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1)), (var.get('l')&Js(268435455)))
        return var.get('c')
    PyJsHoisted_am3_.func_name = 'am3'
    var.put('am3', PyJsHoisted_am3_)
    @Js
    def PyJsHoisted_intAt_(s, i, this, arguments, var=var):
        var = Scope({'s':s, 'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'c', 's'])
        var.put('c', var.get('BI_RC').get(var.get('s').callprop('charCodeAt', var.get('i'))))
        return ((-Js(1.0)) if (var.get('c')==var.get(u"null")) else var.get('c'))
    PyJsHoisted_intAt_.func_name = 'intAt'
    var.put('intAt', PyJsHoisted_intAt_)
    @Js
    def PyJsHoisted_nbv_(i, this, arguments, var=var):
        var = Scope({'i':i, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'r'])
        var.put('r', var.get('nbi')())
        var.get('r').callprop('fromInt', var.get('i'))
        return var.get('r')
    PyJsHoisted_nbv_.func_name = 'nbv'
    var.put('nbv', PyJsHoisted_nbv_)
    @Js
    def PyJsHoisted_nbits_(x, this, arguments, var=var):
        var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
        var.registers(['x', 't', 'r'])
        var.put('r', Js(1.0))
        pass
        if (var.put('t', PyJsBshift(var.get('x'),Js(16.0)))!=Js(0.0)):
            var.put('x', var.get('t'))
            var.put('r', Js(16.0), '+')
        if (var.put('t', (var.get('x')>>Js(8.0)))!=Js(0.0)):
            var.put('x', var.get('t'))
            var.put('r', Js(8.0), '+')
        if (var.put('t', (var.get('x')>>Js(4.0)))!=Js(0.0)):
            var.put('x', var.get('t'))
            var.put('r', Js(4.0), '+')
        if (var.put('t', (var.get('x')>>Js(2.0)))!=Js(0.0)):
            var.put('x', var.get('t'))
            var.put('r', Js(2.0), '+')
        if (var.put('t', (var.get('x')>>Js(1.0)))!=Js(0.0)):
            var.put('x', var.get('t'))
            var.put('r', Js(1.0), '+')
        return var.get('r')
    PyJsHoisted_nbits_.func_name = 'nbits'
    var.put('nbits', PyJsHoisted_nbits_)
    @Js
    def PyJsHoisted_prng_newstate_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        return var.get('Arcfour').create()
    PyJsHoisted_prng_newstate_.func_name = 'prng_newstate'
    var.put('prng_newstate', PyJsHoisted_prng_newstate_)
    @Js
    def PyJsHoisted_rng_get_byte_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['random'])
        if (var.get('rng_state')==var.get(u"null")):
            var.put('rng_state', var.get('prng_newstate')())
            while (var.get('rng_pptr')<var.get('rng_psize')):
                var.put('random', var.get('Math').callprop('floor', (Js(65536.0)*var.get('Math').callprop('random'))))
                var.get('rng_pool').put((var.put('rng_pptr',Js(var.get('rng_pptr').to_number())+Js(1))-Js(1)), (var.get('random')&Js(255.0)))
            var.get('rng_state').callprop('init', var.get('rng_pool'))
            #for JS loop
            var.put('rng_pptr', Js(0.0))
            while (var.get('rng_pptr')<var.get('rng_pool').get('length')):
                try:
                    var.get('rng_pool').put(var.get('rng_pptr'), Js(0.0))
                finally:
                        var.put('rng_pptr',Js(var.get('rng_pptr').to_number())+Js(1))
            var.put('rng_pptr', Js(0.0))
        return var.get('rng_state').callprop('next')
    PyJsHoisted_rng_get_byte_.func_name = 'rng_get_byte'
    var.put('rng_get_byte', PyJsHoisted_rng_get_byte_)
    @Js
    def PyJsHoisted_pkcs1pad1_(s, n, this, arguments, var=var):
        var = Scope({'s':s, 'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['len', 'm', 'filler', 'f', 'n', 's'])
        if (var.get('n')<(var.get('s').get('length')+Js(22.0))):
            var.get('console').callprop('error', Js('Message too long for RSA'))
            return var.get(u"null")
        var.put('len', ((var.get('n')-var.get('s').get('length'))-Js(6.0)))
        var.put('filler', Js(''))
        #for JS loop
        var.put('f', Js(0.0))
        while (var.get('f')<var.get('len')):
            try:
                var.put('filler', Js('ff'), '+')
            finally:
                    var.put('f', Js(2.0), '+')
        var.put('m', (((Js('0001')+var.get('filler'))+Js('00'))+var.get('s')))
        return var.get('parseBigInt')(var.get('m'), Js(16.0))
    PyJsHoisted_pkcs1pad1_.func_name = 'pkcs1pad1'
    var.put('pkcs1pad1', PyJsHoisted_pkcs1pad1_)
    @Js
    def PyJsHoisted_pkcs1pad2_(s, n, this, arguments, var=var):
        var = Scope({'s':s, 'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['x', 'rng', 'c', 'ba', 'i', 'n', 's'])
        if (var.get('n')<(var.get('s').get('length')+Js(11.0))):
            var.get('console').callprop('error', Js('Message too long for RSA'))
            return var.get(u"null")
        var.put('ba', Js([]))
        var.put('i', (var.get('s').get('length')-Js(1.0)))
        while ((var.get('i')>=Js(0.0)) and (var.get('n')>Js(0.0))):
            var.put('c', var.get('s').callprop('charCodeAt', (var.put('i',Js(var.get('i').to_number())-Js(1))+Js(1))))
            if (var.get('c')<Js(128.0)):
                var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), var.get('c'))
            else:
                if ((var.get('c')>Js(127.0)) and (var.get('c')<Js(2048.0))):
                    var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), ((var.get('c')&Js(63.0))|Js(128.0)))
                    var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), ((var.get('c')>>Js(6.0))|Js(192.0)))
                else:
                    var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), ((var.get('c')&Js(63.0))|Js(128.0)))
                    var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), (((var.get('c')>>Js(6.0))&Js(63.0))|Js(128.0)))
                    var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), ((var.get('c')>>Js(12.0))|Js(224.0)))
        var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), Js(0.0))
        var.put('rng', var.get('SecureRandom').create())
        var.put('x', Js([]))
        while (var.get('n')>Js(2.0)):
            var.get('x').put('0', Js(0.0))
            while (var.get('x').get('0')==Js(0.0)):
                var.get('rng').callprop('nextBytes', var.get('x'))
            var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), var.get('x').get('0'))
        var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), Js(2.0))
        var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), Js(0.0))
        return var.get('BigInteger').create(var.get('ba'))
    PyJsHoisted_pkcs1pad2_.func_name = 'pkcs1pad2'
    var.put('pkcs1pad2', PyJsHoisted_pkcs1pad2_)
    @Js
    def PyJsHoisted_pkcs1unpad2_(d, n, this, arguments, var=var):
        var = Scope({'d':d, 'n':n, 'this':this, 'arguments':arguments}, var)
        var.registers(['b', 'd', 'ret', 'c', 'i', 'n'])
        var.put('b', var.get('d').callprop('toByteArray'))
        var.put('i', Js(0.0))
        while ((var.get('i')<var.get('b').get('length')) and (var.get('b').get(var.get('i'))==Js(0.0))):
            var.put('i',Js(var.get('i').to_number())+Js(1))
        if (((var.get('b').get('length')-var.get('i'))!=(var.get('n')-Js(1.0))) or (var.get('b').get(var.get('i'))!=Js(2.0))):
            return var.get(u"null")
        var.put('i',Js(var.get('i').to_number())+Js(1))
        while (var.get('b').get(var.get('i'))!=Js(0.0)):
            if (var.put('i',Js(var.get('i').to_number())+Js(1))>=var.get('b').get('length')):
                return var.get(u"null")
        var.put('ret', Js(''))
        while (var.put('i',Js(var.get('i').to_number())+Js(1))<var.get('b').get('length')):
            var.put('c', (var.get('b').get(var.get('i'))&Js(255.0)))
            if (var.get('c')<Js(128.0)):
                var.put('ret', var.get('String').callprop('fromCharCode', var.get('c')), '+')
            else:
                if ((var.get('c')>Js(191.0)) and (var.get('c')<Js(224.0))):
                    var.put('ret', var.get('String').callprop('fromCharCode', (((var.get('c')&Js(31.0))<<Js(6.0))|(var.get('b').get((var.get('i')+Js(1.0)))&Js(63.0)))), '+')
                    var.put('i',Js(var.get('i').to_number())+Js(1))
                else:
                    var.put('ret', var.get('String').callprop('fromCharCode', ((((var.get('c')&Js(15.0))<<Js(12.0))|((var.get('b').get((var.get('i')+Js(1.0)))&Js(63.0))<<Js(6.0)))|(var.get('b').get((var.get('i')+Js(2.0)))&Js(63.0)))), '+')
                    var.put('i', Js(2.0), '+')
        return var.get('ret')
    PyJsHoisted_pkcs1unpad2_.func_name = 'pkcs1unpad2'
    var.put('pkcs1unpad2', PyJsHoisted_pkcs1unpad2_)
    @Js
    def PyJsHoisted_getDigestHeader_(name, this, arguments, var=var):
        var = Scope({'name':name, 'this':this, 'arguments':arguments}, var)
        var.registers(['name'])
        return (var.get('DIGEST_HEADERS').get(var.get('name')) or Js(''))
    PyJsHoisted_getDigestHeader_.func_name = 'getDigestHeader'
    var.put('getDigestHeader', PyJsHoisted_getDigestHeader_)
    @Js
    def PyJsHoisted_removeDigestHeader_(str, this, arguments, var=var):
        var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
        var.registers(['str', 'name_1', 'header', 'len'])
        for PyJsTemp in var.get('DIGEST_HEADERS'):
            var.put('name_1', PyJsTemp)
            if var.get('DIGEST_HEADERS').callprop('hasOwnProperty', var.get('name_1')):
                var.put('header', var.get('DIGEST_HEADERS').get(var.get('name_1')))
                var.put('len', var.get('header').get('length'))
                if (var.get('str').callprop('substr', Js(0.0), var.get('len'))==var.get('header')):
                    return var.get('str').callprop('substr', var.get('len'))
        return var.get('str')
    PyJsHoisted_removeDigestHeader_.func_name = 'removeDigestHeader'
    var.put('removeDigestHeader', PyJsHoisted_removeDigestHeader_)
    Js('use strict')
    var.put('BI_RM', Js('0123456789abcdefghijklmnopqrstuvwxyz'))
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    var.put('b64map', Js('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'))
    var.put('b64pad', Js('='))
    pass
    pass
    @Js
    def PyJs_anonymous_1_(d, b, this, arguments, var=var):
        var = Scope({'d':d, 'b':b, 'this':this, 'arguments':arguments}, var)
        var.registers(['b', 'd'])
        @Js
        def PyJs_anonymous_2_(d, b, this, arguments, var=var):
            var = Scope({'d':d, 'b':b, 'this':this, 'arguments':arguments}, var)
            var.registers(['b', 'd'])
            var.get('d').put('__proto__', var.get('b'))
        PyJs_anonymous_2_._set_name('anonymous')
        @Js
        def PyJs_anonymous_3_(d, b, this, arguments, var=var):
            var = Scope({'d':d, 'b':b, 'this':this, 'arguments':arguments}, var)
            var.registers(['b', 'p', 'd'])
            for PyJsTemp in var.get('b'):
                var.put('p', PyJsTemp)
                if var.get('b').callprop('hasOwnProperty', var.get('p')):
                    var.get('d').put(var.get('p'), var.get('b').get(var.get('p')))
        PyJs_anonymous_3_._set_name('anonymous')
        var.put('extendStatics', ((var.get('Object').get('setPrototypeOf') or (Js({'__proto__':Js([])}).instanceof(var.get('Array')) and PyJs_anonymous_2_)) or PyJs_anonymous_3_))
        return var.get('extendStatics')(var.get('d'), var.get('b'))
    PyJs_anonymous_1_._set_name('anonymous')
    var.put('extendStatics', PyJs_anonymous_1_)
    pass
    pass
    @Js
    def PyJs_anonymous_4_(a, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['out', 'a', 'c', 'char_count', 'bits', 'i', 'hex', 'ignore'])
        pass
        if PyJsStrictEq(var.get('decoder'),var.get('undefined')):
            var.put('hex', Js('0123456789ABCDEF'))
            var.put('ignore', Js(' \x0c\n\r\t\xa0\u2028\u2029'))
            var.put('decoder', Js({}))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(16.0)):
                try:
                    var.get('decoder').put(var.get('hex').callprop('charAt', var.get('i')), var.get('i'))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            var.put('hex', var.get('hex').callprop('toLowerCase'))
            #for JS loop
            var.put('i', Js(10.0))
            while (var.get('i')<Js(16.0)):
                try:
                    var.get('decoder').put(var.get('hex').callprop('charAt', var.get('i')), var.get('i'))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('ignore').get('length')):
                try:
                    var.get('decoder').put(var.get('ignore').callprop('charAt', var.get('i')), (-Js(1.0)))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
        var.put('out', Js([]))
        var.put('bits', Js(0.0))
        var.put('char_count', Js(0.0))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('a').get('length')):
            try:
                var.put('c', var.get('a').callprop('charAt', var.get('i')))
                if (var.get('c')==Js('=')):
                    break
                var.put('c', var.get('decoder').get(var.get('c')))
                if (var.get('c')==(-Js(1.0))):
                    continue
                if PyJsStrictEq(var.get('c'),var.get('undefined')):
                    PyJsTempException = JsToPyException(var.get('Error').create((Js('Illegal character at offset ')+var.get('i'))))
                    raise PyJsTempException
                var.put('bits', var.get('c'), '|')
                if (var.put('char_count',Js(var.get('char_count').to_number())+Js(1))>=Js(2.0)):
                    var.get('out').put(var.get('out').get('length'), var.get('bits'))
                    var.put('bits', Js(0.0))
                    var.put('char_count', Js(0.0))
                else:
                    var.put('bits', Js(4.0), '<<')
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
        if var.get('char_count'):
            PyJsTempException = JsToPyException(var.get('Error').create(Js('Hex encoding incomplete: 4 bits missing')))
            raise PyJsTempException
        return var.get('out')
    PyJs_anonymous_4_._set_name('anonymous')
    var.put('Hex', Js({'decode':PyJs_anonymous_4_}))
    pass
    @Js
    def PyJs_anonymous_5_(a, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['out', 'a', 'c', 'char_count', 'bits', 'i', 'b64', 'ignore'])
        pass
        if PyJsStrictEq(var.get('decoder$1'),var.get('undefined')):
            var.put('b64', Js('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'))
            var.put('ignore', Js('= \x0c\n\r\t\xa0\u2028\u2029'))
            var.put('decoder$1', var.get('Object').callprop('create', var.get(u"null")))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(64.0)):
                try:
                    var.get('decoder$1').put(var.get('b64').callprop('charAt', var.get('i')), var.get('i'))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('ignore').get('length')):
                try:
                    var.get('decoder$1').put(var.get('ignore').callprop('charAt', var.get('i')), (-Js(1.0)))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
        var.put('out', Js([]))
        var.put('bits', Js(0.0))
        var.put('char_count', Js(0.0))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('a').get('length')):
            try:
                var.put('c', var.get('a').callprop('charAt', var.get('i')))
                if (var.get('c')==Js('=')):
                    break
                var.put('c', var.get('decoder$1').get(var.get('c')))
                if (var.get('c')==(-Js(1.0))):
                    continue
                if PyJsStrictEq(var.get('c'),var.get('undefined')):
                    PyJsTempException = JsToPyException(var.get('Error').create((Js('Illegal character at offset ')+var.get('i'))))
                    raise PyJsTempException
                var.put('bits', var.get('c'), '|')
                if (var.put('char_count',Js(var.get('char_count').to_number())+Js(1))>=Js(4.0)):
                    var.get('out').put(var.get('out').get('length'), (var.get('bits')>>Js(16.0)))
                    var.get('out').put(var.get('out').get('length'), ((var.get('bits')>>Js(8.0))&Js(255)))
                    var.get('out').put(var.get('out').get('length'), (var.get('bits')&Js(255)))
                    var.put('bits', Js(0.0))
                    var.put('char_count', Js(0.0))
                else:
                    var.put('bits', Js(6.0), '<<')
            finally:
                    var.put('i',Js(var.get('i').to_number())+Js(1))
        while 1:
            SWITCHED = False
            CONDITION = (var.get('char_count'))
            if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                SWITCHED = True
                PyJsTempException = JsToPyException(var.get('Error').create(Js('Base64 encoding incomplete: at least 2 bits missing')))
                raise PyJsTempException
            if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                SWITCHED = True
                var.get('out').put(var.get('out').get('length'), (var.get('bits')>>Js(10.0)))
                break
            if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                SWITCHED = True
                var.get('out').put(var.get('out').get('length'), (var.get('bits')>>Js(16.0)))
                var.get('out').put(var.get('out').get('length'), ((var.get('bits')>>Js(8.0))&Js(255)))
                break
            SWITCHED = True
            break
        return var.get('out')
    PyJs_anonymous_5_._set_name('anonymous')
    @Js
    def PyJs_anonymous_6_(a, this, arguments, var=var):
        var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
        var.registers(['a', 'm'])
        var.put('m', var.get('Base64').get('re').callprop('exec', var.get('a')))
        if var.get('m'):
            if var.get('m').get('1'):
                var.put('a', var.get('m').get('1'))
            else:
                if var.get('m').get('2'):
                    var.put('a', var.get('m').get('2'))
                else:
                    PyJsTempException = JsToPyException(var.get('Error').create(Js('RegExp out of sync')))
                    raise PyJsTempException
        return var.get('Base64').callprop('decode', var.get('a'))
    PyJs_anonymous_6_._set_name('anonymous')
    var.put('Base64', Js({'decode':PyJs_anonymous_5_,'re':JsRegExp('/-----BEGIN [^-]+-----([A-Za-z0-9+\\/=\\s]+)-----END [^-]+-----|begin-base64[^\\n]+\\n([A-Za-z0-9+\\/=\\s]+)====/'),'unarmor':PyJs_anonymous_6_}))
    var.put('max', Js(10000000000000.0))
    @Js
    def PyJs_anonymous_7_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['Int10'])
        @Js
        def PyJsHoisted_Int10_(value, this, arguments, var=var):
            var = Scope({'value':value, 'this':this, 'arguments':arguments}, var)
            var.registers(['value'])
            var.get(u"this").put('buf', Js([((+var.get('value')) or Js(0.0))]))
        PyJsHoisted_Int10_.func_name = 'Int10'
        var.put('Int10', PyJsHoisted_Int10_)
        pass
        @Js
        def PyJs_anonymous_8_(m, c, this, arguments, var=var):
            var = Scope({'m':m, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['l', 'b', 'm', 'c', 't', 'i'])
            var.put('b', var.get(u"this").get('buf'))
            var.put('l', var.get('b').get('length'))
            pass
            pass
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('l')):
                try:
                    var.put('t', ((var.get('b').get(var.get('i'))*var.get('m'))+var.get('c')))
                    if (var.get('t')<var.get('max')):
                        var.put('c', Js(0.0))
                    else:
                        var.put('c', (Js(0.0)|(var.get('t')/var.get('max'))))
                        var.put('t', (var.get('c')*var.get('max')), '-')
                    var.get('b').put(var.get('i'), var.get('t'))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            if (var.get('c')>Js(0.0)):
                var.get('b').put(var.get('i'), var.get('c'))
        PyJs_anonymous_8_._set_name('anonymous')
        var.get('Int10').get('prototype').put('mulAdd', PyJs_anonymous_8_)
        @Js
        def PyJs_anonymous_9_(c, this, arguments, var=var):
            var = Scope({'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['l', 'b', 'c', 't', 'i'])
            var.put('b', var.get(u"this").get('buf'))
            var.put('l', var.get('b').get('length'))
            pass
            pass
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('l')):
                try:
                    var.put('t', (var.get('b').get(var.get('i'))-var.get('c')))
                    if (var.get('t')<Js(0.0)):
                        var.put('t', var.get('max'), '+')
                        var.put('c', Js(1.0))
                    else:
                        var.put('c', Js(0.0))
                    var.get('b').put(var.get('i'), var.get('t'))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            while PyJsStrictEq(var.get('b').get((var.get('b').get('length')-Js(1.0))),Js(0.0)):
                var.get('b').callprop('pop')
        PyJs_anonymous_9_._set_name('anonymous')
        var.get('Int10').get('prototype').put('sub', PyJs_anonymous_9_)
        @Js
        def PyJs_anonymous_10_(base, this, arguments, var=var):
            var = Scope({'base':base, 'this':this, 'arguments':arguments}, var)
            var.registers(['base', 'i', 'b', 's'])
            if ((var.get('base') or Js(10.0))!=Js(10.0)):
                PyJsTempException = JsToPyException(var.get('Error').create(Js('only base 10 is supported')))
                raise PyJsTempException
            var.put('b', var.get(u"this").get('buf'))
            var.put('s', var.get('b').get((var.get('b').get('length')-Js(1.0))).callprop('toString'))
            #for JS loop
            var.put('i', (var.get('b').get('length')-Js(2.0)))
            while (var.get('i')>=Js(0.0)):
                try:
                    var.put('s', (var.get('max')+var.get('b').get(var.get('i'))).callprop('toString').callprop('substring', Js(1.0)), '+')
                finally:
                        var.put('i',Js(var.get('i').to_number())-Js(1))
            return var.get('s')
        PyJs_anonymous_10_._set_name('anonymous')
        var.get('Int10').get('prototype').put('toString', PyJs_anonymous_10_)
        @Js
        def PyJs_anonymous_11_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'b', 'v'])
            var.put('b', var.get(u"this").get('buf'))
            var.put('v', Js(0.0))
            #for JS loop
            var.put('i', (var.get('b').get('length')-Js(1.0)))
            while (var.get('i')>=Js(0.0)):
                try:
                    var.put('v', ((var.get('v')*var.get('max'))+var.get('b').get(var.get('i'))))
                finally:
                        var.put('i',Js(var.get('i').to_number())-Js(1))
            return var.get('v')
        PyJs_anonymous_11_._set_name('anonymous')
        var.get('Int10').get('prototype').put('valueOf', PyJs_anonymous_11_)
        @Js
        def PyJs_anonymous_12_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['b'])
            var.put('b', var.get(u"this").get('buf'))
            return (var.get('b').get('0') if (var.get('b').get('length')==Js(1.0)) else var.get(u"this"))
        PyJs_anonymous_12_._set_name('anonymous')
        var.get('Int10').get('prototype').put('simplify', PyJs_anonymous_12_)
        return var.get('Int10')
    PyJs_anonymous_7_._set_name('anonymous')
    var.put('Int10', PyJs_anonymous_7_())
    var.put('ellipsis', Js('\u2026'))
    var.put('reTimeS', JsRegExp('/^(\\d\\d)(0[1-9]|1[0-2])(0[1-9]|[12]\\d|3[01])([01]\\d|2[0-3])(?:([0-5]\\d)(?:([0-5]\\d)(?:[.,](\\d{1,3}))?)?)?(Z|[-+](?:[0]\\d|1[0-2])([0-5]\\d)?)?$/'))
    var.put('reTimeL', JsRegExp('/^(\\d\\d\\d\\d)(0[1-9]|1[0-2])(0[1-9]|[12]\\d|3[01])([01]\\d|2[0-3])(?:([0-5]\\d)(?:([0-5]\\d)(?:[.,](\\d{1,3}))?)?)?(Z|[-+](?:[0]\\d|1[0-2])([0-5]\\d)?)?$/'))
    pass
    @Js
    def PyJs_anonymous_13_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['Stream'])
        @Js
        def PyJsHoisted_Stream_(enc, pos, this, arguments, var=var):
            var = Scope({'enc':enc, 'pos':pos, 'this':this, 'arguments':arguments}, var)
            var.registers(['pos', 'enc'])
            var.get(u"this").put('hexDigits', Js('0123456789ABCDEF'))
            if var.get('enc').instanceof(var.get('Stream')):
                var.get(u"this").put('enc', var.get('enc').get('enc'))
                var.get(u"this").put('pos', var.get('enc').get('pos'))
            else:
                var.get(u"this").put('enc', var.get('enc'))
                var.get(u"this").put('pos', var.get('pos'))
        PyJsHoisted_Stream_.func_name = 'Stream'
        var.put('Stream', PyJsHoisted_Stream_)
        pass
        @Js
        def PyJs_anonymous_14_(pos, this, arguments, var=var):
            var = Scope({'pos':pos, 'this':this, 'arguments':arguments}, var)
            var.registers(['pos'])
            if PyJsStrictEq(var.get('pos'),var.get('undefined')):
                var.put('pos', (var.get(u"this").put('pos',Js(var.get(u"this").get('pos').to_number())+Js(1))-Js(1)))
            if (var.get('pos')>=var.get(u"this").get('enc').get('length')):
                PyJsTempException = JsToPyException(var.get('Error').create((((Js('Requesting byte offset ')+var.get('pos'))+Js(' on a stream of length '))+var.get(u"this").get('enc').get('length'))))
                raise PyJsTempException
            return (var.get(u"this").get('enc').callprop('charCodeAt', var.get('pos')) if PyJsStrictEq(Js('string'),var.get(u"this").get('enc').typeof()) else var.get(u"this").get('enc').get(var.get('pos')))
        PyJs_anonymous_14_._set_name('anonymous')
        var.get('Stream').get('prototype').put('get', PyJs_anonymous_14_)
        @Js
        def PyJs_anonymous_15_(b, this, arguments, var=var):
            var = Scope({'b':b, 'this':this, 'arguments':arguments}, var)
            var.registers(['b'])
            return (var.get(u"this").get('hexDigits').callprop('charAt', ((var.get('b')>>Js(4.0))&Js(15)))+var.get(u"this").get('hexDigits').callprop('charAt', (var.get('b')&Js(15))))
        PyJs_anonymous_15_._set_name('anonymous')
        var.get('Stream').get('prototype').put('hexByte', PyJs_anonymous_15_)
        @Js
        def PyJs_anonymous_16_(start, end, raw, this, arguments, var=var):
            var = Scope({'start':start, 'end':end, 'raw':raw, 'this':this, 'arguments':arguments}, var)
            var.registers(['end', 'raw', 'start', 'i', 's'])
            var.put('s', Js(''))
            #for JS loop
            var.put('i', var.get('start'))
            while (var.get('i')<var.get('end')):
                try:
                    var.put('s', var.get(u"this").callprop('hexByte', var.get(u"this").callprop('get', var.get('i'))), '+')
                    if PyJsStrictNeq(var.get('raw'),Js(True)):
                        while 1:
                            SWITCHED = False
                            CONDITION = ((var.get('i')&Js(15)))
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(7)):
                                SWITCHED = True
                                var.put('s', Js('  '), '+')
                                break
                            if SWITCHED or PyJsStrictEq(CONDITION, Js(15)):
                                SWITCHED = True
                                var.put('s', Js('\n'), '+')
                                break
                            if True:
                                SWITCHED = True
                                var.put('s', Js(' '), '+')
                            SWITCHED = True
                            break
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return var.get('s')
        PyJs_anonymous_16_._set_name('anonymous')
        var.get('Stream').get('prototype').put('hexDump', PyJs_anonymous_16_)
        @Js
        def PyJs_anonymous_17_(start, end, this, arguments, var=var):
            var = Scope({'start':start, 'end':end, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'start', 'end', 'c'])
            #for JS loop
            var.put('i', var.get('start'))
            while (var.get('i')<var.get('end')):
                try:
                    var.put('c', var.get(u"this").callprop('get', var.get('i')))
                    if ((var.get('c')<Js(32.0)) or (var.get('c')>Js(176.0))):
                        return Js(False)
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return Js(True)
        PyJs_anonymous_17_._set_name('anonymous')
        var.get('Stream').get('prototype').put('isASCII', PyJs_anonymous_17_)
        @Js
        def PyJs_anonymous_18_(start, end, this, arguments, var=var):
            var = Scope({'start':start, 'end':end, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'start', 'end', 's'])
            var.put('s', Js(''))
            #for JS loop
            var.put('i', var.get('start'))
            while (var.get('i')<var.get('end')):
                try:
                    var.put('s', var.get('String').callprop('fromCharCode', var.get(u"this").callprop('get', var.get('i'))), '+')
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return var.get('s')
        PyJs_anonymous_18_._set_name('anonymous')
        var.get('Stream').get('prototype').put('parseStringISO', PyJs_anonymous_18_)
        @Js
        def PyJs_anonymous_19_(start, end, this, arguments, var=var):
            var = Scope({'start':start, 'end':end, 'this':this, 'arguments':arguments}, var)
            var.registers(['end', 'c', 'start', 'i', 's'])
            var.put('s', Js(''))
            #for JS loop
            var.put('i', var.get('start'))
            while (var.get('i')<var.get('end')):
                var.put('c', var.get(u"this").callprop('get', (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))))
                if (var.get('c')<Js(128.0)):
                    var.put('s', var.get('String').callprop('fromCharCode', var.get('c')), '+')
                else:
                    if ((var.get('c')>Js(191.0)) and (var.get('c')<Js(224.0))):
                        var.put('s', var.get('String').callprop('fromCharCode', (((var.get('c')&Js(31))<<Js(6.0))|(var.get(u"this").callprop('get', (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)))&Js(63)))), '+')
                    else:
                        var.put('s', var.get('String').callprop('fromCharCode', ((((var.get('c')&Js(15))<<Js(12.0))|((var.get(u"this").callprop('get', (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)))&Js(63))<<Js(6.0)))|(var.get(u"this").callprop('get', (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)))&Js(63)))), '+')
            
            return var.get('s')
        PyJs_anonymous_19_._set_name('anonymous')
        var.get('Stream').get('prototype').put('parseStringUTF', PyJs_anonymous_19_)
        @Js
        def PyJs_anonymous_20_(start, end, this, arguments, var=var):
            var = Scope({'start':start, 'end':end, 'this':this, 'arguments':arguments}, var)
            var.registers(['end', 'hi', 'start', 'i', 'lo', 'str'])
            var.put('str', Js(''))
            pass
            pass
            #for JS loop
            var.put('i', var.get('start'))
            while (var.get('i')<var.get('end')):
                var.put('hi', var.get(u"this").callprop('get', (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))))
                var.put('lo', var.get(u"this").callprop('get', (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))))
                var.put('str', var.get('String').callprop('fromCharCode', ((var.get('hi')<<Js(8.0))|var.get('lo'))), '+')
            
            return var.get('str')
        PyJs_anonymous_20_._set_name('anonymous')
        var.get('Stream').get('prototype').put('parseStringBMP', PyJs_anonymous_20_)
        @Js
        def PyJs_anonymous_21_(start, end, shortYear, this, arguments, var=var):
            var = Scope({'start':start, 'end':end, 'shortYear':shortYear, 'this':this, 'arguments':arguments}, var)
            var.registers(['end', 'shortYear', 'm', 'start', 's'])
            var.put('s', var.get(u"this").callprop('parseStringISO', var.get('start'), var.get('end')))
            var.put('m', (var.get('reTimeS') if var.get('shortYear') else var.get('reTimeL')).callprop('exec', var.get('s')))
            if var.get('m').neg():
                return (Js('Unrecognized time: ')+var.get('s'))
            if var.get('shortYear'):
                var.get('m').put('1', (+var.get('m').get('1')))
                var.get('m').put('1', (Js(2000.0) if ((+var.get('m').get('1'))<Js(70.0)) else Js(1900.0)), '+')
            var.put('s', ((((((var.get('m').get('1')+Js('-'))+var.get('m').get('2'))+Js('-'))+var.get('m').get('3'))+Js(' '))+var.get('m').get('4')))
            if var.get('m').get('5'):
                var.put('s', (Js(':')+var.get('m').get('5')), '+')
                if var.get('m').get('6'):
                    var.put('s', (Js(':')+var.get('m').get('6')), '+')
                    if var.get('m').get('7'):
                        var.put('s', (Js('.')+var.get('m').get('7')), '+')
            if var.get('m').get('8'):
                var.put('s', Js(' UTC'), '+')
                if (var.get('m').get('8')!=Js('Z')):
                    var.put('s', var.get('m').get('8'), '+')
                    if var.get('m').get('9'):
                        var.put('s', (Js(':')+var.get('m').get('9')), '+')
            return var.get('s')
        PyJs_anonymous_21_._set_name('anonymous')
        var.get('Stream').get('prototype').put('parseTime', PyJs_anonymous_21_)
        @Js
        def PyJs_anonymous_22_(start, end, this, arguments, var=var):
            var = Scope({'start':start, 'end':end, 'this':this, 'arguments':arguments}, var)
            var.registers(['end', 'len', 'start', 'v', 'pad', 'n', 'i', 'neg', 's'])
            var.put('v', var.get(u"this").callprop('get', var.get('start')))
            var.put('neg', (var.get('v')>Js(127.0)))
            var.put('pad', (Js(255.0) if var.get('neg') else Js(0.0)))
            pass
            var.put('s', Js(''))
            while ((var.get('v')==var.get('pad')) and (var.put('start',Js(var.get('start').to_number())+Js(1))<var.get('end'))):
                var.put('v', var.get(u"this").callprop('get', var.get('start')))
            var.put('len', (var.get('end')-var.get('start')))
            if PyJsStrictEq(var.get('len'),Js(0.0)):
                return ((-Js(1.0)) if var.get('neg') else Js(0.0))
            if (var.get('len')>Js(4.0)):
                var.put('s', var.get('v'))
                var.put('len', Js(3.0), '<<')
                while ((((+var.get('s'))^var.get('pad'))&Js(128))==Js(0.0)):
                    var.put('s', ((+var.get('s'))<<Js(1.0)))
                    var.put('len',Js(var.get('len').to_number())-Js(1))
                var.put('s', ((Js('(')+var.get('len'))+Js(' bit)\n')))
            if var.get('neg'):
                var.put('v', (var.get('v')-Js(256.0)))
            var.put('n', var.get('Int10').create(var.get('v')))
            #for JS loop
            var.put('i', (var.get('start')+Js(1.0)))
            while (var.get('i')<var.get('end')):
                try:
                    var.get('n').callprop('mulAdd', Js(256.0), var.get(u"this").callprop('get', var.get('i')))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return (var.get('s')+var.get('n').callprop('toString'))
        PyJs_anonymous_22_._set_name('anonymous')
        var.get('Stream').get('prototype').put('parseInteger', PyJs_anonymous_22_)
        @Js
        def PyJs_anonymous_23_(start, end, maxLength, this, arguments, var=var):
            var = Scope({'start':start, 'end':end, 'maxLength':maxLength, 'this':this, 'arguments':arguments}, var)
            var.registers(['b', 'end', 'skip', 'unusedBit', 'lenBit', 'start', 'maxLength', 'intro', 'i', 'j', 's'])
            var.put('unusedBit', var.get(u"this").callprop('get', var.get('start')))
            var.put('lenBit', ((((var.get('end')-var.get('start'))-Js(1.0))<<Js(3.0))-var.get('unusedBit')))
            var.put('intro', ((Js('(')+var.get('lenBit'))+Js(' bit)\n')))
            var.put('s', Js(''))
            #for JS loop
            var.put('i', (var.get('start')+Js(1.0)))
            while (var.get('i')<var.get('end')):
                try:
                    var.put('b', var.get(u"this").callprop('get', var.get('i')))
                    var.put('skip', (var.get('unusedBit') if (var.get('i')==(var.get('end')-Js(1.0))) else Js(0.0)))
                    #for JS loop
                    var.put('j', Js(7.0))
                    while (var.get('j')>=var.get('skip')):
                        try:
                            var.put('s', (Js('1') if ((var.get('b')>>var.get('j'))&Js(1.0)) else Js('0')), '+')
                        finally:
                                var.put('j',Js(var.get('j').to_number())-Js(1))
                    if (var.get('s').get('length')>var.get('maxLength')):
                        return (var.get('intro')+var.get('stringCut')(var.get('s'), var.get('maxLength')))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return (var.get('intro')+var.get('s'))
        PyJs_anonymous_23_._set_name('anonymous')
        var.get('Stream').get('prototype').put('parseBitString', PyJs_anonymous_23_)
        @Js
        def PyJs_anonymous_24_(start, end, maxLength, this, arguments, var=var):
            var = Scope({'start':start, 'end':end, 'maxLength':maxLength, 'this':this, 'arguments':arguments}, var)
            var.registers(['end', 'len', 'start', 'maxLength', 'i', 's'])
            if var.get(u"this").callprop('isASCII', var.get('start'), var.get('end')):
                return var.get('stringCut')(var.get(u"this").callprop('parseStringISO', var.get('start'), var.get('end')), var.get('maxLength'))
            var.put('len', (var.get('end')-var.get('start')))
            var.put('s', ((Js('(')+var.get('len'))+Js(' byte)\n')))
            var.put('maxLength', Js(2.0), '/')
            if (var.get('len')>var.get('maxLength')):
                var.put('end', (var.get('start')+var.get('maxLength')))
            #for JS loop
            var.put('i', var.get('start'))
            while (var.get('i')<var.get('end')):
                try:
                    var.put('s', var.get(u"this").callprop('hexByte', var.get(u"this").callprop('get', var.get('i'))), '+')
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            if (var.get('len')>var.get('maxLength')):
                var.put('s', var.get('ellipsis'), '+')
            return var.get('s')
        PyJs_anonymous_24_._set_name('anonymous')
        var.get('Stream').get('prototype').put('parseOctetString', PyJs_anonymous_24_)
        @Js
        def PyJs_anonymous_25_(start, end, maxLength, this, arguments, var=var):
            var = Scope({'start':start, 'end':end, 'maxLength':maxLength, 'this':this, 'arguments':arguments}, var)
            var.registers(['end', 'm', 'start', 'v', 'maxLength', 'bits', 'i', 'n', 's'])
            var.put('s', Js(''))
            var.put('n', var.get('Int10').create())
            var.put('bits', Js(0.0))
            #for JS loop
            var.put('i', var.get('start'))
            while (var.get('i')<var.get('end')):
                try:
                    var.put('v', var.get(u"this").callprop('get', var.get('i')))
                    var.get('n').callprop('mulAdd', Js(128.0), (var.get('v')&Js(127)))
                    var.put('bits', Js(7.0), '+')
                    if (var.get('v')&Js(128)).neg():
                        if PyJsStrictEq(var.get('s'),Js('')):
                            var.put('n', var.get('n').callprop('simplify'))
                            if var.get('n').instanceof(var.get('Int10')):
                                var.get('n').callprop('sub', Js(80.0))
                                var.put('s', (Js('2.')+var.get('n').callprop('toString')))
                            else:
                                var.put('m', ((Js(0.0) if (var.get('n')<Js(40.0)) else Js(1.0)) if (var.get('n')<Js(80.0)) else Js(2.0)))
                                var.put('s', ((var.get('m')+Js('.'))+(var.get('n')-(var.get('m')*Js(40.0)))))
                        else:
                            var.put('s', (Js('.')+var.get('n').callprop('toString')), '+')
                        if (var.get('s').get('length')>var.get('maxLength')):
                            return var.get('stringCut')(var.get('s'), var.get('maxLength'))
                        var.put('n', var.get('Int10').create())
                        var.put('bits', Js(0.0))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            if (var.get('bits')>Js(0.0)):
                var.put('s', Js('.incomplete'), '+')
            return var.get('s')
        PyJs_anonymous_25_._set_name('anonymous')
        var.get('Stream').get('prototype').put('parseOID', PyJs_anonymous_25_)
        return var.get('Stream')
    PyJs_anonymous_13_._set_name('anonymous')
    var.put('Stream', PyJs_anonymous_13_())
    @Js
    def PyJs_anonymous_26_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['ASN1'])
        @Js
        def PyJsHoisted_ASN1_(stream, header, length, tag, sub, this, arguments, var=var):
            var = Scope({'stream':stream, 'header':header, 'length':length, 'tag':tag, 'sub':sub, 'this':this, 'arguments':arguments}, var)
            var.registers(['stream', 'tag', 'header', 'length', 'sub'])
            if var.get('tag').instanceof(var.get('ASN1Tag')).neg():
                PyJsTempException = JsToPyException(var.get('Error').create(Js('Invalid tag value.')))
                raise PyJsTempException
            var.get(u"this").put('stream', var.get('stream'))
            var.get(u"this").put('header', var.get('header'))
            var.get(u"this").put('length', var.get('length'))
            var.get(u"this").put('tag', var.get('tag'))
            var.get(u"this").put('sub', var.get('sub'))
        PyJsHoisted_ASN1_.func_name = 'ASN1'
        var.put('ASN1', PyJsHoisted_ASN1_)
        pass
        @Js
        def PyJs_anonymous_27_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            while 1:
                SWITCHED = False
                CONDITION = (var.get(u"this").get('tag').get('tagClass'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
                    SWITCHED = True
                    while 1:
                        SWITCHED = False
                        CONDITION = (var.get(u"this").get('tag').get('tagNumber'))
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(0)):
                            SWITCHED = True
                            return Js('EOC')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(1)):
                            SWITCHED = True
                            return Js('BOOLEAN')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(2)):
                            SWITCHED = True
                            return Js('INTEGER')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(3)):
                            SWITCHED = True
                            return Js('BIT_STRING')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(4)):
                            SWITCHED = True
                            return Js('OCTET_STRING')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(5)):
                            SWITCHED = True
                            return Js('NULL')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(6)):
                            SWITCHED = True
                            return Js('OBJECT_IDENTIFIER')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(7)):
                            SWITCHED = True
                            return Js('ObjectDescriptor')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(8)):
                            SWITCHED = True
                            return Js('EXTERNAL')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(9)):
                            SWITCHED = True
                            return Js('REAL')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(10)):
                            SWITCHED = True
                            return Js('ENUMERATED')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(11)):
                            SWITCHED = True
                            return Js('EMBEDDED_PDV')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(12)):
                            SWITCHED = True
                            return Js('UTF8String')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(16)):
                            SWITCHED = True
                            return Js('SEQUENCE')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(17)):
                            SWITCHED = True
                            return Js('SET')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(18)):
                            SWITCHED = True
                            return Js('NumericString')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(19)):
                            SWITCHED = True
                            return Js('PrintableString')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(20)):
                            SWITCHED = True
                            return Js('TeletexString')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(21)):
                            SWITCHED = True
                            return Js('VideotexString')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(22)):
                            SWITCHED = True
                            return Js('IA5String')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(23)):
                            SWITCHED = True
                            return Js('UTCTime')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(24)):
                            SWITCHED = True
                            return Js('GeneralizedTime')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(25)):
                            SWITCHED = True
                            return Js('GraphicString')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(26)):
                            SWITCHED = True
                            return Js('VisibleString')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(27)):
                            SWITCHED = True
                            return Js('GeneralString')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(28)):
                            SWITCHED = True
                            return Js('UniversalString')
                        if SWITCHED or PyJsStrictEq(CONDITION, Js(30)):
                            SWITCHED = True
                            return Js('BMPString')
                        SWITCHED = True
                        break
                    return (Js('Universal_')+var.get(u"this").get('tag').get('tagNumber').callprop('toString'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
                    SWITCHED = True
                    return (Js('Application_')+var.get(u"this").get('tag').get('tagNumber').callprop('toString'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
                    SWITCHED = True
                    return ((Js('[')+var.get(u"this").get('tag').get('tagNumber').callprop('toString'))+Js(']'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
                    SWITCHED = True
                    return (Js('Private_')+var.get(u"this").get('tag').get('tagNumber').callprop('toString'))
                SWITCHED = True
                break
        PyJs_anonymous_27_._set_name('anonymous')
        var.get('ASN1').get('prototype').put('typeName', PyJs_anonymous_27_)
        @Js
        def PyJs_anonymous_28_(maxLength, this, arguments, var=var):
            var = Scope({'maxLength':maxLength, 'this':this, 'arguments':arguments}, var)
            var.registers(['content', 'maxLength', 'len'])
            if PyJsStrictEq(var.get(u"this").get('tag'),var.get('undefined')):
                return var.get(u"null")
            if PyJsStrictEq(var.get('maxLength'),var.get('undefined')):
                var.put('maxLength', var.get('Infinity'))
            var.put('content', var.get(u"this").callprop('posContent'))
            var.put('len', var.get('Math').callprop('abs', var.get(u"this").get('length')))
            if var.get(u"this").get('tag').callprop('isUniversal').neg():
                if PyJsStrictNeq(var.get(u"this").get('sub'),var.get(u"null")):
                    return ((Js('(')+var.get(u"this").get('sub').get('length'))+Js(' elem)'))
                return var.get(u"this").get('stream').callprop('parseOctetString', var.get('content'), (var.get('content')+var.get('len')), var.get('maxLength'))
            while 1:
                SWITCHED = False
                CONDITION = (var.get(u"this").get('tag').get('tagNumber'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(1)):
                    SWITCHED = True
                    return (Js('false') if PyJsStrictEq(var.get(u"this").get('stream').callprop('get', var.get('content')),Js(0.0)) else Js('true'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(2)):
                    SWITCHED = True
                    return var.get(u"this").get('stream').callprop('parseInteger', var.get('content'), (var.get('content')+var.get('len')))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(3)):
                    SWITCHED = True
                    return (((Js('(')+var.get(u"this").get('sub').get('length'))+Js(' elem)')) if var.get(u"this").get('sub') else var.get(u"this").get('stream').callprop('parseBitString', var.get('content'), (var.get('content')+var.get('len')), var.get('maxLength')))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(4)):
                    SWITCHED = True
                    return (((Js('(')+var.get(u"this").get('sub').get('length'))+Js(' elem)')) if var.get(u"this").get('sub') else var.get(u"this").get('stream').callprop('parseOctetString', var.get('content'), (var.get('content')+var.get('len')), var.get('maxLength')))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(6)):
                    SWITCHED = True
                    return var.get(u"this").get('stream').callprop('parseOID', var.get('content'), (var.get('content')+var.get('len')), var.get('maxLength'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(16)):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, Js(17)):
                    SWITCHED = True
                    if PyJsStrictNeq(var.get(u"this").get('sub'),var.get(u"null")):
                        return ((Js('(')+var.get(u"this").get('sub').get('length'))+Js(' elem)'))
                    else:
                        return Js('(no elem)')
                if SWITCHED or PyJsStrictEq(CONDITION, Js(12)):
                    SWITCHED = True
                    return var.get('stringCut')(var.get(u"this").get('stream').callprop('parseStringUTF', var.get('content'), (var.get('content')+var.get('len'))), var.get('maxLength'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(18)):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, Js(19)):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, Js(20)):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, Js(21)):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, Js(22)):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, Js(26)):
                    SWITCHED = True
                    return var.get('stringCut')(var.get(u"this").get('stream').callprop('parseStringISO', var.get('content'), (var.get('content')+var.get('len'))), var.get('maxLength'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(30)):
                    SWITCHED = True
                    return var.get('stringCut')(var.get(u"this").get('stream').callprop('parseStringBMP', var.get('content'), (var.get('content')+var.get('len'))), var.get('maxLength'))
                if SWITCHED or PyJsStrictEq(CONDITION, Js(23)):
                    SWITCHED = True
                    pass
                if SWITCHED or PyJsStrictEq(CONDITION, Js(24)):
                    SWITCHED = True
                    return var.get(u"this").get('stream').callprop('parseTime', var.get('content'), (var.get('content')+var.get('len')), (var.get(u"this").get('tag').get('tagNumber')==Js(23)))
                SWITCHED = True
                break
            return var.get(u"null")
        PyJs_anonymous_28_._set_name('anonymous')
        var.get('ASN1').get('prototype').put('content', PyJs_anonymous_28_)
        @Js
        def PyJs_anonymous_29_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return (((((((((var.get(u"this").callprop('typeName')+Js('@'))+var.get(u"this").get('stream').get('pos'))+Js('[header:'))+var.get(u"this").get('header'))+Js(',length:'))+var.get(u"this").get('length'))+Js(',sub:'))+(Js('null') if PyJsStrictEq(var.get(u"this").get('sub'),var.get(u"null")) else var.get(u"this").get('sub').get('length')))+Js(']'))
        PyJs_anonymous_29_._set_name('anonymous')
        var.get('ASN1').get('prototype').put('toString', PyJs_anonymous_29_)
        @Js
        def PyJs_anonymous_30_(indent, this, arguments, var=var):
            var = Scope({'indent':indent, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'indent', 'max', 's'])
            if PyJsStrictEq(var.get('indent'),var.get('undefined')):
                var.put('indent', Js(''))
            var.put('s', (((var.get('indent')+var.get(u"this").callprop('typeName'))+Js(' @'))+var.get(u"this").get('stream').get('pos')))
            if (var.get(u"this").get('length')>=Js(0.0)):
                var.put('s', Js('+'), '+')
            var.put('s', var.get(u"this").get('length'), '+')
            if var.get(u"this").get('tag').get('tagConstructed'):
                var.put('s', Js(' (constructed)'), '+')
            else:
                if ((var.get(u"this").get('tag').callprop('isUniversal') and ((var.get(u"this").get('tag').get('tagNumber')==Js(3)) or (var.get(u"this").get('tag').get('tagNumber')==Js(4)))) and PyJsStrictNeq(var.get(u"this").get('sub'),var.get(u"null"))):
                    var.put('s', Js(' (encapsulates)'), '+')
            var.put('s', Js('\n'), '+')
            if PyJsStrictNeq(var.get(u"this").get('sub'),var.get(u"null")):
                var.put('indent', Js('  '), '+')
                #for JS loop
                var.put('i', Js(0.0))
                var.put('max', var.get(u"this").get('sub').get('length'))
                while (var.get('i')<var.get('max')):
                    try:
                        var.put('s', var.get(u"this").get('sub').get(var.get('i')).callprop('toPrettyString', var.get('indent')), '+')
                    finally:
                            var.put('i',Js(var.get('i').to_number())+Js(1))
            return var.get('s')
        PyJs_anonymous_30_._set_name('anonymous')
        var.get('ASN1').get('prototype').put('toPrettyString', PyJs_anonymous_30_)
        @Js
        def PyJs_anonymous_31_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return var.get(u"this").get('stream').get('pos')
        PyJs_anonymous_31_._set_name('anonymous')
        var.get('ASN1').get('prototype').put('posStart', PyJs_anonymous_31_)
        @Js
        def PyJs_anonymous_32_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return (var.get(u"this").get('stream').get('pos')+var.get(u"this").get('header'))
        PyJs_anonymous_32_._set_name('anonymous')
        var.get('ASN1').get('prototype').put('posContent', PyJs_anonymous_32_)
        @Js
        def PyJs_anonymous_33_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return ((var.get(u"this").get('stream').get('pos')+var.get(u"this").get('header'))+var.get('Math').callprop('abs', var.get(u"this").get('length')))
        PyJs_anonymous_33_._set_name('anonymous')
        var.get('ASN1').get('prototype').put('posEnd', PyJs_anonymous_33_)
        @Js
        def PyJs_anonymous_34_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return var.get(u"this").get('stream').callprop('hexDump', var.get(u"this").callprop('posStart'), var.get(u"this").callprop('posEnd'), Js(True))
        PyJs_anonymous_34_._set_name('anonymous')
        var.get('ASN1').get('prototype').put('toHexString', PyJs_anonymous_34_)
        @Js
        def PyJs_anonymous_35_(stream, this, arguments, var=var):
            var = Scope({'stream':stream, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'stream', 'len', 'buf'])
            var.put('buf', var.get('stream').callprop('get'))
            var.put('len', (var.get('buf')&Js(127)))
            if (var.get('len')==var.get('buf')):
                return var.get('len')
            if (var.get('len')>Js(6.0)):
                PyJsTempException = JsToPyException(var.get('Error').create((Js('Length over 48 bits not supported at position ')+(var.get('stream').get('pos')-Js(1.0)))))
                raise PyJsTempException
            if PyJsStrictEq(var.get('len'),Js(0.0)):
                return var.get(u"null")
            var.put('buf', Js(0.0))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('len')):
                try:
                    var.put('buf', ((var.get('buf')*Js(256.0))+var.get('stream').callprop('get')))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return var.get('buf')
        PyJs_anonymous_35_._set_name('anonymous')
        var.get('ASN1').put('decodeLength', PyJs_anonymous_35_)
        @Js
        def PyJs_anonymous_36_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['hexString', 'length', 'offset'])
            var.put('hexString', var.get(u"this").callprop('toHexString'))
            var.put('offset', (var.get(u"this").get('header')*Js(2.0)))
            var.put('length', (var.get(u"this").get('length')*Js(2.0)))
            return var.get('hexString').callprop('substr', var.get('offset'), var.get('length'))
        PyJs_anonymous_36_._set_name('anonymous')
        var.get('ASN1').get('prototype').put('getHexStringValue', PyJs_anonymous_36_)
        @Js
        def PyJs_anonymous_37_(str, this, arguments, var=var):
            var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
            var.registers(['stream', 'tag', 'len', 'sub', 'header', 'i', 'start', 'getSub', 'str', 'streamStart'])
            pass
            if var.get('str').instanceof(var.get('Stream')).neg():
                var.put('stream', var.get('Stream').create(var.get('str'), Js(0.0)))
            else:
                var.put('stream', var.get('str'))
            var.put('streamStart', var.get('Stream').create(var.get('stream')))
            var.put('tag', var.get('ASN1Tag').create(var.get('stream')))
            var.put('len', var.get('ASN1').callprop('decodeLength', var.get('stream')))
            var.put('start', var.get('stream').get('pos'))
            var.put('header', (var.get('start')-var.get('streamStart').get('pos')))
            var.put('sub', var.get(u"null"))
            @Js
            def PyJs_anonymous_38_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments}, var)
                var.registers(['ret', 'end', 's'])
                var.put('ret', Js([]))
                if PyJsStrictNeq(var.get('len'),var.get(u"null")):
                    var.put('end', (var.get('start')+var.get('len')))
                    while (var.get('stream').get('pos')<var.get('end')):
                        var.get('ret').put(var.get('ret').get('length'), var.get('ASN1').callprop('decode', var.get('stream')))
                    if (var.get('stream').get('pos')!=var.get('end')):
                        PyJsTempException = JsToPyException(var.get('Error').create((Js('Content size is not correct for container starting at offset ')+var.get('start'))))
                        raise PyJsTempException
                else:
                    try:
                        #for JS loop
                        
                        while 1:
                            var.put('s', var.get('ASN1').callprop('decode', var.get('stream')))
                            if var.get('s').get('tag').callprop('isEOC'):
                                break
                            var.get('ret').put(var.get('ret').get('length'), var.get('s'))
                        
                        var.put('len', (var.get('start')-var.get('stream').get('pos')))
                    except PyJsException as PyJsTempException:
                        PyJsHolder_65_42289986 = var.own.get('e')
                        var.force_own_put('e', PyExceptionToJs(PyJsTempException))
                        try:
                            PyJsTempException = JsToPyException(var.get('Error').create((Js('Exception while decoding undefined length content: ')+var.get('e'))))
                            raise PyJsTempException
                        finally:
                            if PyJsHolder_65_42289986 is not None:
                                var.own['e'] = PyJsHolder_65_42289986
                            else:
                                del var.own['e']
                            del PyJsHolder_65_42289986
                return var.get('ret')
            PyJs_anonymous_38_._set_name('anonymous')
            var.put('getSub', PyJs_anonymous_38_)
            if var.get('tag').get('tagConstructed'):
                var.put('sub', var.get('getSub')())
            else:
                if (var.get('tag').callprop('isUniversal') and ((var.get('tag').get('tagNumber')==Js(3)) or (var.get('tag').get('tagNumber')==Js(4)))):
                    try:
                        if (var.get('tag').get('tagNumber')==Js(3)):
                            if (var.get('stream').callprop('get')!=Js(0.0)):
                                PyJsTempException = JsToPyException(var.get('Error').create(Js('BIT STRINGs with unused bits cannot encapsulate.')))
                                raise PyJsTempException
                        var.put('sub', var.get('getSub')())
                        #for JS loop
                        var.put('i', Js(0.0))
                        while (var.get('i')<var.get('sub').get('length')):
                            try:
                                if var.get('sub').get(var.get('i')).get('tag').callprop('isEOC'):
                                    PyJsTempException = JsToPyException(var.get('Error').create(Js('EOC is not supposed to be actual content.')))
                                    raise PyJsTempException
                            finally:
                                    var.put('i',Js(var.get('i').to_number())+Js(1))
                    except PyJsException as PyJsTempException:
                        PyJsHolder_65_49388852 = var.own.get('e')
                        var.force_own_put('e', PyExceptionToJs(PyJsTempException))
                        try:
                            var.put('sub', var.get(u"null"))
                        finally:
                            if PyJsHolder_65_49388852 is not None:
                                var.own['e'] = PyJsHolder_65_49388852
                            else:
                                del var.own['e']
                            del PyJsHolder_65_49388852
            if PyJsStrictEq(var.get('sub'),var.get(u"null")):
                if PyJsStrictEq(var.get('len'),var.get(u"null")):
                    PyJsTempException = JsToPyException(var.get('Error').create((Js("We can't skip over an invalid tag with undefined length at offset ")+var.get('start'))))
                    raise PyJsTempException
                var.get('stream').put('pos', (var.get('start')+var.get('Math').callprop('abs', var.get('len'))))
            return var.get('ASN1').create(var.get('streamStart'), var.get('header'), var.get('len'), var.get('tag'), var.get('sub'))
        PyJs_anonymous_37_._set_name('anonymous')
        var.get('ASN1').put('decode', PyJs_anonymous_37_)
        return var.get('ASN1')
    PyJs_anonymous_26_._set_name('anonymous')
    var.put('ASN1', PyJs_anonymous_26_())
    @Js
    def PyJs_anonymous_39_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['ASN1Tag'])
        @Js
        def PyJsHoisted_ASN1Tag_(stream, this, arguments, var=var):
            var = Scope({'stream':stream, 'this':this, 'arguments':arguments}, var)
            var.registers(['n', 'stream', 'buf'])
            var.put('buf', var.get('stream').callprop('get'))
            var.get(u"this").put('tagClass', (var.get('buf')>>Js(6.0)))
            var.get(u"this").put('tagConstructed', PyJsStrictNeq((var.get('buf')&Js(32)),Js(0.0)))
            var.get(u"this").put('tagNumber', (var.get('buf')&Js(31)))
            if (var.get(u"this").get('tagNumber')==Js(31)):
                var.put('n', var.get('Int10').create())
                while 1:
                    var.put('buf', var.get('stream').callprop('get'))
                    var.get('n').callprop('mulAdd', Js(128.0), (var.get('buf')&Js(127)))
                    if not (var.get('buf')&Js(128)):
                        break
                var.get(u"this").put('tagNumber', var.get('n').callprop('simplify'))
        PyJsHoisted_ASN1Tag_.func_name = 'ASN1Tag'
        var.put('ASN1Tag', PyJsHoisted_ASN1Tag_)
        pass
        @Js
        def PyJs_anonymous_40_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return PyJsStrictEq(var.get(u"this").get('tagClass'),Js(0))
        PyJs_anonymous_40_._set_name('anonymous')
        var.get('ASN1Tag').get('prototype').put('isUniversal', PyJs_anonymous_40_)
        @Js
        def PyJs_anonymous_41_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return (PyJsStrictEq(var.get(u"this").get('tagClass'),Js(0)) and PyJsStrictEq(var.get(u"this").get('tagNumber'),Js(0)))
        PyJs_anonymous_41_._set_name('anonymous')
        var.get('ASN1Tag').get('prototype').put('isEOC', PyJs_anonymous_41_)
        return var.get('ASN1Tag')
    PyJs_anonymous_39_._set_name('anonymous')
    var.put('ASN1Tag', PyJs_anonymous_39_())
    pass
    var.put('canary', Js(244837814094590))
    var.put('j_lm', ((var.get('canary')&Js(16777215))==Js(15715070)))
    var.put('lowprimes', Js([Js(2.0), Js(3.0), Js(5.0), Js(7.0), Js(11.0), Js(13.0), Js(17.0), Js(19.0), Js(23.0), Js(29.0), Js(31.0), Js(37.0), Js(41.0), Js(43.0), Js(47.0), Js(53.0), Js(59.0), Js(61.0), Js(67.0), Js(71.0), Js(73.0), Js(79.0), Js(83.0), Js(89.0), Js(97.0), Js(101.0), Js(103.0), Js(107.0), Js(109.0), Js(113.0), Js(127.0), Js(131.0), Js(137.0), Js(139.0), Js(149.0), Js(151.0), Js(157.0), Js(163.0), Js(167.0), Js(173.0), Js(179.0), Js(181.0), Js(191.0), Js(193.0), Js(197.0), Js(199.0), Js(211.0), Js(223.0), Js(227.0), Js(229.0), Js(233.0), Js(239.0), Js(241.0), Js(251.0), Js(257.0), Js(263.0), Js(269.0), Js(271.0), Js(277.0), Js(281.0), Js(283.0), Js(293.0), Js(307.0), Js(311.0), Js(313.0), Js(317.0), Js(331.0), Js(337.0), Js(347.0), Js(349.0), Js(353.0), Js(359.0), Js(367.0), Js(373.0), Js(379.0), Js(383.0), Js(389.0), Js(397.0), Js(401.0), Js(409.0), Js(419.0), Js(421.0), Js(431.0), Js(433.0), Js(439.0), Js(443.0), Js(449.0), Js(457.0), Js(461.0), Js(463.0), Js(467.0), Js(479.0), Js(487.0), Js(491.0), Js(499.0), Js(503.0), Js(509.0), Js(521.0), Js(523.0), Js(541.0), Js(547.0), Js(557.0), Js(563.0), Js(569.0), Js(571.0), Js(577.0), Js(587.0), Js(593.0), Js(599.0), Js(601.0), Js(607.0), Js(613.0), Js(617.0), Js(619.0), Js(631.0), Js(641.0), Js(643.0), Js(647.0), Js(653.0), Js(659.0), Js(661.0), Js(673.0), Js(677.0), Js(683.0), Js(691.0), Js(701.0), Js(709.0), Js(719.0), Js(727.0), Js(733.0), Js(739.0), Js(743.0), Js(751.0), Js(757.0), Js(761.0), Js(769.0), Js(773.0), Js(787.0), Js(797.0), Js(809.0), Js(811.0), Js(821.0), Js(823.0), Js(827.0), Js(829.0), Js(839.0), Js(853.0), Js(857.0), Js(859.0), Js(863.0), Js(877.0), Js(881.0), Js(883.0), Js(887.0), Js(907.0), Js(911.0), Js(919.0), Js(929.0), Js(937.0), Js(941.0), Js(947.0), Js(953.0), Js(967.0), Js(971.0), Js(977.0), Js(983.0), Js(991.0), Js(997.0)]))
    var.put('lplim', ((Js(1.0)<<Js(26.0))/var.get('lowprimes').get((var.get('lowprimes').get('length')-Js(1.0)))))
    @Js
    def PyJs_anonymous_42_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['BigInteger'])
        @Js
        def PyJsHoisted_BigInteger_(a, b, c, this, arguments, var=var):
            var = Scope({'a':a, 'b':b, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['b', 'a', 'c'])
            if (var.get('a')!=var.get(u"null")):
                if (Js('number')==var.get('a',throw=False).typeof()):
                    var.get(u"this").callprop('fromNumber', var.get('a'), var.get('b'), var.get('c'))
                else:
                    if ((var.get('b')==var.get(u"null")) and (Js('string')!=var.get('a',throw=False).typeof())):
                        var.get(u"this").callprop('fromString', var.get('a'), Js(256.0))
                    else:
                        var.get(u"this").callprop('fromString', var.get('a'), var.get('b'))
        PyJsHoisted_BigInteger_.func_name = 'BigInteger'
        var.put('BigInteger', PyJsHoisted_BigInteger_)
        pass
        @Js
        def PyJs_anonymous_43_(b, this, arguments, var=var):
            var = Scope({'b':b, 'this':this, 'arguments':arguments}, var)
            var.registers(['b', 'p', 'k', 'd', 'm', 'km', 'r', 'i'])
            if (var.get(u"this").get('s')<Js(0.0)):
                return (Js('-')+var.get(u"this").callprop('negate').callprop('toString', var.get('b')))
            pass
            if (var.get('b')==Js(16.0)):
                var.put('k', Js(4.0))
            else:
                if (var.get('b')==Js(8.0)):
                    var.put('k', Js(3.0))
                else:
                    if (var.get('b')==Js(2.0)):
                        var.put('k', Js(1.0))
                    else:
                        if (var.get('b')==Js(32.0)):
                            var.put('k', Js(5.0))
                        else:
                            if (var.get('b')==Js(4.0)):
                                var.put('k', Js(2.0))
                            else:
                                return var.get(u"this").callprop('toRadix', var.get('b'))
            var.put('km', ((Js(1.0)<<var.get('k'))-Js(1.0)))
            pass
            var.put('m', Js(False))
            var.put('r', Js(''))
            var.put('i', var.get(u"this").get('t'))
            var.put('p', (var.get(u"this").get('DB')-((var.get('i')*var.get(u"this").get('DB'))%var.get('k'))))
            if ((var.put('i',Js(var.get('i').to_number())-Js(1))+Js(1))>Js(0.0)):
                if ((var.get('p')<var.get(u"this").get('DB')) and (var.put('d', (var.get(u"this").get(var.get('i'))>>var.get('p')))>Js(0.0))):
                    var.put('m', Js(True))
                    var.put('r', var.get('int2char')(var.get('d')))
                while (var.get('i')>=Js(0.0)):
                    if (var.get('p')<var.get('k')):
                        var.put('d', ((var.get(u"this").get(var.get('i'))&((Js(1.0)<<var.get('p'))-Js(1.0)))<<(var.get('k')-var.get('p'))))
                        var.put('d', (var.get(u"this").get(var.put('i',Js(var.get('i').to_number())-Js(1)))>>var.put('p', (var.get(u"this").get('DB')-var.get('k')), '+')), '|')
                    else:
                        var.put('d', ((var.get(u"this").get(var.get('i'))>>var.put('p', var.get('k'), '-'))&var.get('km')))
                        if (var.get('p')<=Js(0.0)):
                            var.put('p', var.get(u"this").get('DB'), '+')
                            var.put('i',Js(var.get('i').to_number())-Js(1))
                    if (var.get('d')>Js(0.0)):
                        var.put('m', Js(True))
                    if var.get('m'):
                        var.put('r', var.get('int2char')(var.get('d')), '+')
            return (var.get('r') if var.get('m') else Js('0'))
        PyJs_anonymous_43_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('toString', PyJs_anonymous_43_)
        @Js
        def PyJs_anonymous_44_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['r'])
            var.put('r', var.get('nbi')())
            var.get('BigInteger').get('ZERO').callprop('subTo', var.get(u"this"), var.get('r'))
            return var.get('r')
        PyJs_anonymous_44_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('negate', PyJs_anonymous_44_)
        @Js
        def PyJs_anonymous_45_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return (var.get(u"this").callprop('negate') if (var.get(u"this").get('s')<Js(0.0)) else var.get(u"this"))
        PyJs_anonymous_45_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('abs', PyJs_anonymous_45_)
        @Js
        def PyJs_anonymous_46_(a, this, arguments, var=var):
            var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'a', 'r'])
            var.put('r', (var.get(u"this").get('s')-var.get('a').get('s')))
            if (var.get('r')!=Js(0.0)):
                return var.get('r')
            var.put('i', var.get(u"this").get('t'))
            var.put('r', (var.get('i')-var.get('a').get('t')))
            if (var.get('r')!=Js(0.0)):
                return ((-var.get('r')) if (var.get(u"this").get('s')<Js(0.0)) else var.get('r'))
            while (var.put('i',Js(var.get('i').to_number())-Js(1))>=Js(0.0)):
                if (var.put('r', (var.get(u"this").get(var.get('i'))-var.get('a').get(var.get('i'))))!=Js(0.0)):
                    return var.get('r')
            return Js(0.0)
        PyJs_anonymous_46_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('compareTo', PyJs_anonymous_46_)
        @Js
        def PyJs_anonymous_47_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            if (var.get(u"this").get('t')<=Js(0.0)):
                return Js(0.0)
            return ((var.get(u"this").get('DB')*(var.get(u"this").get('t')-Js(1.0)))+var.get('nbits')((var.get(u"this").get((var.get(u"this").get('t')-Js(1.0)))^(var.get(u"this").get('s')&var.get(u"this").get('DM')))))
        PyJs_anonymous_47_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('bitLength', PyJs_anonymous_47_)
        @Js
        def PyJs_anonymous_48_(a, this, arguments, var=var):
            var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'r'])
            var.put('r', var.get('nbi')())
            var.get(u"this").callprop('abs').callprop('divRemTo', var.get('a'), var.get(u"null"), var.get('r'))
            if ((var.get(u"this").get('s')<Js(0.0)) and (var.get('r').callprop('compareTo', var.get('BigInteger').get('ZERO'))>Js(0.0))):
                var.get('a').callprop('subTo', var.get('r'), var.get('r'))
            return var.get('r')
        PyJs_anonymous_48_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('mod', PyJs_anonymous_48_)
        @Js
        def PyJs_anonymous_49_(e, m, this, arguments, var=var):
            var = Scope({'e':e, 'm':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['z', 'e', 'm'])
            pass
            if ((var.get('e')<Js(256.0)) or var.get('m').callprop('isEven')):
                var.put('z', var.get('Classic').create(var.get('m')))
            else:
                var.put('z', var.get('Montgomery').create(var.get('m')))
            return var.get(u"this").callprop('exp', var.get('e'), var.get('z'))
        PyJs_anonymous_49_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('modPowInt', PyJs_anonymous_49_)
        @Js
        def PyJs_anonymous_50_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['r'])
            var.put('r', var.get('nbi')())
            var.get(u"this").callprop('copyTo', var.get('r'))
            return var.get('r')
        PyJs_anonymous_50_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('clone', PyJs_anonymous_50_)
        @Js
        def PyJs_anonymous_51_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            if (var.get(u"this").get('s')<Js(0.0)):
                if (var.get(u"this").get('t')==Js(1.0)):
                    return (var.get(u"this").get('0')-var.get(u"this").get('DV'))
                else:
                    if (var.get(u"this").get('t')==Js(0.0)):
                        return (-Js(1.0))
            else:
                if (var.get(u"this").get('t')==Js(1.0)):
                    return var.get(u"this").get('0')
                else:
                    if (var.get(u"this").get('t')==Js(0.0)):
                        return Js(0.0)
            return (((var.get(u"this").get('1')&((Js(1.0)<<(Js(32.0)-var.get(u"this").get('DB')))-Js(1.0)))<<var.get(u"this").get('DB'))|var.get(u"this").get('0'))
        PyJs_anonymous_51_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('intValue', PyJs_anonymous_51_)
        @Js
        def PyJs_anonymous_52_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return (var.get(u"this").get('s') if (var.get(u"this").get('t')==Js(0.0)) else ((var.get(u"this").get('0')<<Js(24.0))>>Js(24.0)))
        PyJs_anonymous_52_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('byteValue', PyJs_anonymous_52_)
        @Js
        def PyJs_anonymous_53_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return (var.get(u"this").get('s') if (var.get(u"this").get('t')==Js(0.0)) else ((var.get(u"this").get('0')<<Js(16.0))>>Js(16.0)))
        PyJs_anonymous_53_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('shortValue', PyJs_anonymous_53_)
        @Js
        def PyJs_anonymous_54_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            if (var.get(u"this").get('s')<Js(0.0)):
                return (-Js(1.0))
            else:
                if ((var.get(u"this").get('t')<=Js(0.0)) or ((var.get(u"this").get('t')==Js(1.0)) and (var.get(u"this").get('0')<=Js(0.0)))):
                    return Js(0.0)
                else:
                    return Js(1.0)
        PyJs_anonymous_54_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('signum', PyJs_anonymous_54_)
        @Js
        def PyJs_anonymous_55_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['p', 'k', 'd', 'r', 'i'])
            var.put('i', var.get(u"this").get('t'))
            var.put('r', Js([]))
            var.get('r').put('0', var.get(u"this").get('s'))
            var.put('p', (var.get(u"this").get('DB')-((var.get('i')*var.get(u"this").get('DB'))%Js(8.0))))
            pass
            var.put('k', Js(0.0))
            if ((var.put('i',Js(var.get('i').to_number())-Js(1))+Js(1))>Js(0.0)):
                if ((var.get('p')<var.get(u"this").get('DB')) and (var.put('d', (var.get(u"this").get(var.get('i'))>>var.get('p')))!=((var.get(u"this").get('s')&var.get(u"this").get('DM'))>>var.get('p')))):
                    var.get('r').put((var.put('k',Js(var.get('k').to_number())+Js(1))-Js(1)), (var.get('d')|(var.get(u"this").get('s')<<(var.get(u"this").get('DB')-var.get('p')))))
                while (var.get('i')>=Js(0.0)):
                    if (var.get('p')<Js(8.0)):
                        var.put('d', ((var.get(u"this").get(var.get('i'))&((Js(1.0)<<var.get('p'))-Js(1.0)))<<(Js(8.0)-var.get('p'))))
                        var.put('d', (var.get(u"this").get(var.put('i',Js(var.get('i').to_number())-Js(1)))>>var.put('p', (var.get(u"this").get('DB')-Js(8.0)), '+')), '|')
                    else:
                        var.put('d', ((var.get(u"this").get(var.get('i'))>>var.put('p', Js(8.0), '-'))&Js(255)))
                        if (var.get('p')<=Js(0.0)):
                            var.put('p', var.get(u"this").get('DB'), '+')
                            var.put('i',Js(var.get('i').to_number())-Js(1))
                    if ((var.get('d')&Js(128))!=Js(0.0)):
                        var.put('d', (-Js(256.0)), '|')
                    if ((var.get('k')==Js(0.0)) and ((var.get(u"this").get('s')&Js(128))!=(var.get('d')&Js(128)))):
                        var.put('k',Js(var.get('k').to_number())+Js(1))
                    if ((var.get('k')>Js(0.0)) or (var.get('d')!=var.get(u"this").get('s'))):
                        var.get('r').put((var.put('k',Js(var.get('k').to_number())+Js(1))-Js(1)), var.get('d'))
            return var.get('r')
        PyJs_anonymous_55_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('toByteArray', PyJs_anonymous_55_)
        @Js
        def PyJs_anonymous_56_(a, this, arguments, var=var):
            var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
            var.registers(['a'])
            return (var.get(u"this").callprop('compareTo', var.get('a'))==Js(0.0))
        PyJs_anonymous_56_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('equals', PyJs_anonymous_56_)
        @Js
        def PyJs_anonymous_57_(a, this, arguments, var=var):
            var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
            var.registers(['a'])
            return (var.get(u"this") if (var.get(u"this").callprop('compareTo', var.get('a'))<Js(0.0)) else var.get('a'))
        PyJs_anonymous_57_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('min', PyJs_anonymous_57_)
        @Js
        def PyJs_anonymous_58_(a, this, arguments, var=var):
            var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
            var.registers(['a'])
            return (var.get(u"this") if (var.get(u"this").callprop('compareTo', var.get('a'))>Js(0.0)) else var.get('a'))
        PyJs_anonymous_58_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('max', PyJs_anonymous_58_)
        @Js
        def PyJs_anonymous_59_(a, this, arguments, var=var):
            var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'r'])
            var.put('r', var.get('nbi')())
            var.get(u"this").callprop('bitwiseTo', var.get('a'), var.get('op_and'), var.get('r'))
            return var.get('r')
        PyJs_anonymous_59_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('and', PyJs_anonymous_59_)
        @Js
        def PyJs_anonymous_60_(a, this, arguments, var=var):
            var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'r'])
            var.put('r', var.get('nbi')())
            var.get(u"this").callprop('bitwiseTo', var.get('a'), var.get('op_or'), var.get('r'))
            return var.get('r')
        PyJs_anonymous_60_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('or', PyJs_anonymous_60_)
        @Js
        def PyJs_anonymous_61_(a, this, arguments, var=var):
            var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'r'])
            var.put('r', var.get('nbi')())
            var.get(u"this").callprop('bitwiseTo', var.get('a'), var.get('op_xor'), var.get('r'))
            return var.get('r')
        PyJs_anonymous_61_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('xor', PyJs_anonymous_61_)
        @Js
        def PyJs_anonymous_62_(a, this, arguments, var=var):
            var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'r'])
            var.put('r', var.get('nbi')())
            var.get(u"this").callprop('bitwiseTo', var.get('a'), var.get('op_andnot'), var.get('r'))
            return var.get('r')
        PyJs_anonymous_62_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('andNot', PyJs_anonymous_62_)
        @Js
        def PyJs_anonymous_63_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'r'])
            var.put('r', var.get('nbi')())
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get(u"this").get('t')):
                try:
                    var.get('r').put(var.get('i'), (var.get(u"this").get('DM')&(~var.get(u"this").get(var.get('i')))))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            var.get('r').put('t', var.get(u"this").get('t'))
            var.get('r').put('s', (~var.get(u"this").get('s')))
            return var.get('r')
        PyJs_anonymous_63_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('not', PyJs_anonymous_63_)
        @Js
        def PyJs_anonymous_64_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n', 'r'])
            var.put('r', var.get('nbi')())
            if (var.get('n')<Js(0.0)):
                var.get(u"this").callprop('rShiftTo', (-var.get('n')), var.get('r'))
            else:
                var.get(u"this").callprop('lShiftTo', var.get('n'), var.get('r'))
            return var.get('r')
        PyJs_anonymous_64_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('shiftLeft', PyJs_anonymous_64_)
        @Js
        def PyJs_anonymous_65_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n', 'r'])
            var.put('r', var.get('nbi')())
            if (var.get('n')<Js(0.0)):
                var.get(u"this").callprop('lShiftTo', (-var.get('n')), var.get('r'))
            else:
                var.get(u"this").callprop('rShiftTo', var.get('n'), var.get('r'))
            return var.get('r')
        PyJs_anonymous_65_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('shiftRight', PyJs_anonymous_65_)
        @Js
        def PyJs_anonymous_66_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['i'])
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get(u"this").get('t')):
                try:
                    if (var.get(u"this").get(var.get('i'))!=Js(0.0)):
                        return ((var.get('i')*var.get(u"this").get('DB'))+var.get('lbit')(var.get(u"this").get(var.get('i'))))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            if (var.get(u"this").get('s')<Js(0.0)):
                return (var.get(u"this").get('t')*var.get(u"this").get('DB'))
            return (-Js(1.0))
        PyJs_anonymous_66_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('getLowestSetBit', PyJs_anonymous_66_)
        @Js
        def PyJs_anonymous_67_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'x', 'r'])
            var.put('r', Js(0.0))
            var.put('x', (var.get(u"this").get('s')&var.get(u"this").get('DM')))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get(u"this").get('t')):
                try:
                    var.put('r', var.get('cbit')((var.get(u"this").get(var.get('i'))^var.get('x'))), '+')
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return var.get('r')
        PyJs_anonymous_67_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('bitCount', PyJs_anonymous_67_)
        @Js
        def PyJs_anonymous_68_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['j', 'n'])
            var.put('j', var.get('Math').callprop('floor', (var.get('n')/var.get(u"this").get('DB'))))
            if (var.get('j')>=var.get(u"this").get('t')):
                return (var.get(u"this").get('s')!=Js(0.0))
            return ((var.get(u"this").get(var.get('j'))&(Js(1.0)<<(var.get('n')%var.get(u"this").get('DB'))))!=Js(0.0))
        PyJs_anonymous_68_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('testBit', PyJs_anonymous_68_)
        @Js
        def PyJs_anonymous_69_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return var.get(u"this").callprop('changeBit', var.get('n'), var.get('op_or'))
        PyJs_anonymous_69_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('setBit', PyJs_anonymous_69_)
        @Js
        def PyJs_anonymous_70_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return var.get(u"this").callprop('changeBit', var.get('n'), var.get('op_andnot'))
        PyJs_anonymous_70_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('clearBit', PyJs_anonymous_70_)
        @Js
        def PyJs_anonymous_71_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            return var.get(u"this").callprop('changeBit', var.get('n'), var.get('op_xor'))
        PyJs_anonymous_71_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('flipBit', PyJs_anonymous_71_)
        @Js
        def PyJs_anonymous_72_(a, this, arguments, var=var):
            var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'r'])
            var.put('r', var.get('nbi')())
            var.get(u"this").callprop('addTo', var.get('a'), var.get('r'))
            return var.get('r')
        PyJs_anonymous_72_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('add', PyJs_anonymous_72_)
        @Js
        def PyJs_anonymous_73_(a, this, arguments, var=var):
            var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'r'])
            var.put('r', var.get('nbi')())
            var.get(u"this").callprop('subTo', var.get('a'), var.get('r'))
            return var.get('r')
        PyJs_anonymous_73_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('subtract', PyJs_anonymous_73_)
        @Js
        def PyJs_anonymous_74_(a, this, arguments, var=var):
            var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'r'])
            var.put('r', var.get('nbi')())
            var.get(u"this").callprop('multiplyTo', var.get('a'), var.get('r'))
            return var.get('r')
        PyJs_anonymous_74_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('multiply', PyJs_anonymous_74_)
        @Js
        def PyJs_anonymous_75_(a, this, arguments, var=var):
            var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'r'])
            var.put('r', var.get('nbi')())
            var.get(u"this").callprop('divRemTo', var.get('a'), var.get('r'), var.get(u"null"))
            return var.get('r')
        PyJs_anonymous_75_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('divide', PyJs_anonymous_75_)
        @Js
        def PyJs_anonymous_76_(a, this, arguments, var=var):
            var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'r'])
            var.put('r', var.get('nbi')())
            var.get(u"this").callprop('divRemTo', var.get('a'), var.get(u"null"), var.get('r'))
            return var.get('r')
        PyJs_anonymous_76_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('remainder', PyJs_anonymous_76_)
        @Js
        def PyJs_anonymous_77_(a, this, arguments, var=var):
            var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'r', 'q'])
            var.put('q', var.get('nbi')())
            var.put('r', var.get('nbi')())
            var.get(u"this").callprop('divRemTo', var.get('a'), var.get('q'), var.get('r'))
            return Js([var.get('q'), var.get('r')])
        PyJs_anonymous_77_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('divideAndRemainder', PyJs_anonymous_77_)
        @Js
        def PyJs_anonymous_78_(e, m, this, arguments, var=var):
            var = Scope({'e':e, 'm':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['g', 'k', 'w', 'm', 'r2', 'km', 'r', 'k1', 'g2', 'is1', 't', 'z', 'i', 'j', 'n', 'e'])
            var.put('i', var.get('e').callprop('bitLength'))
            pass
            var.put('r', var.get('nbv')(Js(1.0)))
            pass
            if (var.get('i')<=Js(0.0)):
                return var.get('r')
            else:
                if (var.get('i')<Js(18.0)):
                    var.put('k', Js(1.0))
                else:
                    if (var.get('i')<Js(48.0)):
                        var.put('k', Js(3.0))
                    else:
                        if (var.get('i')<Js(144.0)):
                            var.put('k', Js(4.0))
                        else:
                            if (var.get('i')<Js(768.0)):
                                var.put('k', Js(5.0))
                            else:
                                var.put('k', Js(6.0))
            if (var.get('i')<Js(8.0)):
                var.put('z', var.get('Classic').create(var.get('m')))
            else:
                if var.get('m').callprop('isEven'):
                    var.put('z', var.get('Barrett').create(var.get('m')))
                else:
                    var.put('z', var.get('Montgomery').create(var.get('m')))
            var.put('g', Js([]))
            var.put('n', Js(3.0))
            var.put('k1', (var.get('k')-Js(1.0)))
            var.put('km', ((Js(1.0)<<var.get('k'))-Js(1.0)))
            var.get('g').put('1', var.get('z').callprop('convert', var.get(u"this")))
            if (var.get('k')>Js(1.0)):
                var.put('g2', var.get('nbi')())
                var.get('z').callprop('sqrTo', var.get('g').get('1'), var.get('g2'))
                while (var.get('n')<=var.get('km')):
                    var.get('g').put(var.get('n'), var.get('nbi')())
                    var.get('z').callprop('mulTo', var.get('g2'), var.get('g').get((var.get('n')-Js(2.0))), var.get('g').get(var.get('n')))
                    var.put('n', Js(2.0), '+')
            var.put('j', (var.get('e').get('t')-Js(1.0)))
            pass
            var.put('is1', Js(True))
            var.put('r2', var.get('nbi')())
            pass
            var.put('i', (var.get('nbits')(var.get('e').get(var.get('j')))-Js(1.0)))
            while (var.get('j')>=Js(0.0)):
                if (var.get('i')>=var.get('k1')):
                    var.put('w', ((var.get('e').get(var.get('j'))>>(var.get('i')-var.get('k1')))&var.get('km')))
                else:
                    var.put('w', ((var.get('e').get(var.get('j'))&((Js(1.0)<<(var.get('i')+Js(1.0)))-Js(1.0)))<<(var.get('k1')-var.get('i'))))
                    if (var.get('j')>Js(0.0)):
                        var.put('w', (var.get('e').get((var.get('j')-Js(1.0)))>>((var.get(u"this").get('DB')+var.get('i'))-var.get('k1'))), '|')
                var.put('n', var.get('k'))
                while ((var.get('w')&Js(1.0))==Js(0.0)):
                    var.put('w', Js(1.0), '>>')
                    var.put('n',Js(var.get('n').to_number())-Js(1))
                if (var.put('i', var.get('n'), '-')<Js(0.0)):
                    var.put('i', var.get(u"this").get('DB'), '+')
                    var.put('j',Js(var.get('j').to_number())-Js(1))
                if var.get('is1'):
                    var.get('g').get(var.get('w')).callprop('copyTo', var.get('r'))
                    var.put('is1', Js(False))
                else:
                    while (var.get('n')>Js(1.0)):
                        var.get('z').callprop('sqrTo', var.get('r'), var.get('r2'))
                        var.get('z').callprop('sqrTo', var.get('r2'), var.get('r'))
                        var.put('n', Js(2.0), '-')
                    if (var.get('n')>Js(0.0)):
                        var.get('z').callprop('sqrTo', var.get('r'), var.get('r2'))
                    else:
                        var.put('t', var.get('r'))
                        var.put('r', var.get('r2'))
                        var.put('r2', var.get('t'))
                    var.get('z').callprop('mulTo', var.get('r2'), var.get('g').get(var.get('w')), var.get('r'))
                while ((var.get('j')>=Js(0.0)) and ((var.get('e').get(var.get('j'))&(Js(1.0)<<var.get('i')))==Js(0.0))):
                    var.get('z').callprop('sqrTo', var.get('r'), var.get('r2'))
                    var.put('t', var.get('r'))
                    var.put('r', var.get('r2'))
                    var.put('r2', var.get('t'))
                    if (var.put('i',Js(var.get('i').to_number())-Js(1))<Js(0.0)):
                        var.put('i', (var.get(u"this").get('DB')-Js(1.0)))
                        var.put('j',Js(var.get('j').to_number())-Js(1))
            return var.get('z').callprop('revert', var.get('r'))
        PyJs_anonymous_78_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('modPow', PyJs_anonymous_78_)
        @Js
        def PyJs_anonymous_79_(m, this, arguments, var=var):
            var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['b', 'd', 'm', 'a', 'u', 'c', 'v', 'ac'])
            var.put('ac', var.get('m').callprop('isEven'))
            if ((var.get(u"this").callprop('isEven') and var.get('ac')) or (var.get('m').callprop('signum')==Js(0.0))):
                return var.get('BigInteger').get('ZERO')
            var.put('u', var.get('m').callprop('clone'))
            var.put('v', var.get(u"this").callprop('clone'))
            var.put('a', var.get('nbv')(Js(1.0)))
            var.put('b', var.get('nbv')(Js(0.0)))
            var.put('c', var.get('nbv')(Js(0.0)))
            var.put('d', var.get('nbv')(Js(1.0)))
            while (var.get('u').callprop('signum')!=Js(0.0)):
                while var.get('u').callprop('isEven'):
                    var.get('u').callprop('rShiftTo', Js(1.0), var.get('u'))
                    if var.get('ac'):
                        if (var.get('a').callprop('isEven').neg() or var.get('b').callprop('isEven').neg()):
                            var.get('a').callprop('addTo', var.get(u"this"), var.get('a'))
                            var.get('b').callprop('subTo', var.get('m'), var.get('b'))
                        var.get('a').callprop('rShiftTo', Js(1.0), var.get('a'))
                    else:
                        if var.get('b').callprop('isEven').neg():
                            var.get('b').callprop('subTo', var.get('m'), var.get('b'))
                    var.get('b').callprop('rShiftTo', Js(1.0), var.get('b'))
                while var.get('v').callprop('isEven'):
                    var.get('v').callprop('rShiftTo', Js(1.0), var.get('v'))
                    if var.get('ac'):
                        if (var.get('c').callprop('isEven').neg() or var.get('d').callprop('isEven').neg()):
                            var.get('c').callprop('addTo', var.get(u"this"), var.get('c'))
                            var.get('d').callprop('subTo', var.get('m'), var.get('d'))
                        var.get('c').callprop('rShiftTo', Js(1.0), var.get('c'))
                    else:
                        if var.get('d').callprop('isEven').neg():
                            var.get('d').callprop('subTo', var.get('m'), var.get('d'))
                    var.get('d').callprop('rShiftTo', Js(1.0), var.get('d'))
                if (var.get('u').callprop('compareTo', var.get('v'))>=Js(0.0)):
                    var.get('u').callprop('subTo', var.get('v'), var.get('u'))
                    if var.get('ac'):
                        var.get('a').callprop('subTo', var.get('c'), var.get('a'))
                    var.get('b').callprop('subTo', var.get('d'), var.get('b'))
                else:
                    var.get('v').callprop('subTo', var.get('u'), var.get('v'))
                    if var.get('ac'):
                        var.get('c').callprop('subTo', var.get('a'), var.get('c'))
                    var.get('d').callprop('subTo', var.get('b'), var.get('d'))
            if (var.get('v').callprop('compareTo', var.get('BigInteger').get('ONE'))!=Js(0.0)):
                return var.get('BigInteger').get('ZERO')
            if (var.get('d').callprop('compareTo', var.get('m'))>=Js(0.0)):
                return var.get('d').callprop('subtract', var.get('m'))
            if (var.get('d').callprop('signum')<Js(0.0)):
                var.get('d').callprop('addTo', var.get('m'), var.get('d'))
            else:
                return var.get('d')
            if (var.get('d').callprop('signum')<Js(0.0)):
                return var.get('d').callprop('add', var.get('m'))
            else:
                return var.get('d')
        PyJs_anonymous_79_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('modInverse', PyJs_anonymous_79_)
        @Js
        def PyJs_anonymous_80_(e, this, arguments, var=var):
            var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['e'])
            return var.get(u"this").callprop('exp', var.get('e'), var.get('NullExp').create())
        PyJs_anonymous_80_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('pow', PyJs_anonymous_80_)
        @Js
        def PyJs_anonymous_81_(a, this, arguments, var=var):
            var = Scope({'a':a, 'this':this, 'arguments':arguments}, var)
            var.registers(['x', 'g', 'a', 't', 'y', 'i'])
            var.put('x', (var.get(u"this").callprop('negate') if (var.get(u"this").get('s')<Js(0.0)) else var.get(u"this").callprop('clone')))
            var.put('y', (var.get('a').callprop('negate') if (var.get('a').get('s')<Js(0.0)) else var.get('a').callprop('clone')))
            if (var.get('x').callprop('compareTo', var.get('y'))<Js(0.0)):
                var.put('t', var.get('x'))
                var.put('x', var.get('y'))
                var.put('y', var.get('t'))
            var.put('i', var.get('x').callprop('getLowestSetBit'))
            var.put('g', var.get('y').callprop('getLowestSetBit'))
            if (var.get('g')<Js(0.0)):
                return var.get('x')
            if (var.get('i')<var.get('g')):
                var.put('g', var.get('i'))
            if (var.get('g')>Js(0.0)):
                var.get('x').callprop('rShiftTo', var.get('g'), var.get('x'))
                var.get('y').callprop('rShiftTo', var.get('g'), var.get('y'))
            while (var.get('x').callprop('signum')>Js(0.0)):
                if (var.put('i', var.get('x').callprop('getLowestSetBit'))>Js(0.0)):
                    var.get('x').callprop('rShiftTo', var.get('i'), var.get('x'))
                if (var.put('i', var.get('y').callprop('getLowestSetBit'))>Js(0.0)):
                    var.get('y').callprop('rShiftTo', var.get('i'), var.get('y'))
                if (var.get('x').callprop('compareTo', var.get('y'))>=Js(0.0)):
                    var.get('x').callprop('subTo', var.get('y'), var.get('x'))
                    var.get('x').callprop('rShiftTo', Js(1.0), var.get('x'))
                else:
                    var.get('y').callprop('subTo', var.get('x'), var.get('y'))
                    var.get('y').callprop('rShiftTo', Js(1.0), var.get('y'))
            if (var.get('g')>Js(0.0)):
                var.get('y').callprop('lShiftTo', var.get('g'), var.get('y'))
            return var.get('y')
        PyJs_anonymous_81_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('gcd', PyJs_anonymous_81_)
        @Js
        def PyJs_anonymous_82_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['x', 'm', 't', 'i', 'j'])
            pass
            var.put('x', var.get(u"this").callprop('abs'))
            if ((var.get('x').get('t')==Js(1.0)) and (var.get('x').get('0')<=var.get('lowprimes').get((var.get('lowprimes').get('length')-Js(1.0))))):
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('lowprimes').get('length')):
                    try:
                        if (var.get('x').get('0')==var.get('lowprimes').get(var.get('i'))):
                            return Js(True)
                    finally:
                            var.put('i',Js(var.get('i').to_number())+Js(1))
                return Js(False)
            if var.get('x').callprop('isEven'):
                return Js(False)
            var.put('i', Js(1.0))
            while (var.get('i')<var.get('lowprimes').get('length')):
                var.put('m', var.get('lowprimes').get(var.get('i')))
                var.put('j', (var.get('i')+Js(1.0)))
                while ((var.get('j')<var.get('lowprimes').get('length')) and (var.get('m')<var.get('lplim'))):
                    var.put('m', var.get('lowprimes').get((var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))), '*')
                var.put('m', var.get('x').callprop('modInt', var.get('m')))
                while (var.get('i')<var.get('j')):
                    if ((var.get('m')%var.get('lowprimes').get((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))))==Js(0.0)):
                        return Js(False)
            return var.get('x').callprop('millerRabin', var.get('t'))
        PyJs_anonymous_82_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('isProbablePrime', PyJs_anonymous_82_)
        @Js
        def PyJs_anonymous_83_(r, this, arguments, var=var):
            var = Scope({'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'r'])
            #for JS loop
            var.put('i', (var.get(u"this").get('t')-Js(1.0)))
            while (var.get('i')>=Js(0.0)):
                try:
                    var.get('r').put(var.get('i'), var.get(u"this").get(var.get('i')))
                finally:
                        var.put('i',Js(var.get('i').to_number())-Js(1))
            var.get('r').put('t', var.get(u"this").get('t'))
            var.get('r').put('s', var.get(u"this").get('s'))
        PyJs_anonymous_83_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('copyTo', PyJs_anonymous_83_)
        @Js
        def PyJs_anonymous_84_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x'])
            var.get(u"this").put('t', Js(1.0))
            var.get(u"this").put('s', ((-Js(1.0)) if (var.get('x')<Js(0.0)) else Js(0.0)))
            if (var.get('x')>Js(0.0)):
                var.get(u"this").put('0', var.get('x'))
            else:
                if (var.get('x')<(-Js(1.0))):
                    var.get(u"this").put('0', (var.get('x')+var.get(u"this").get('DV')))
                else:
                    var.get(u"this").put('t', Js(0.0))
        PyJs_anonymous_84_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('fromInt', PyJs_anonymous_84_)
        @Js
        def PyJs_anonymous_85_(s, b, this, arguments, var=var):
            var = Scope({'s':s, 'b':b, 'this':this, 'arguments':arguments}, var)
            var.registers(['x', 'b', 'k', 'sh', 'mi', 'i', 's'])
            pass
            if (var.get('b')==Js(16.0)):
                var.put('k', Js(4.0))
            else:
                if (var.get('b')==Js(8.0)):
                    var.put('k', Js(3.0))
                else:
                    if (var.get('b')==Js(256.0)):
                        var.put('k', Js(8.0))
                    else:
                        if (var.get('b')==Js(2.0)):
                            var.put('k', Js(1.0))
                        else:
                            if (var.get('b')==Js(32.0)):
                                var.put('k', Js(5.0))
                            else:
                                if (var.get('b')==Js(4.0)):
                                    var.put('k', Js(2.0))
                                else:
                                    var.get(u"this").callprop('fromRadix', var.get('s'), var.get('b'))
                                    return var.get('undefined')
            var.get(u"this").put('t', Js(0.0))
            var.get(u"this").put('s', Js(0.0))
            var.put('i', var.get('s').get('length'))
            var.put('mi', Js(False))
            var.put('sh', Js(0.0))
            while (var.put('i',Js(var.get('i').to_number())-Js(1))>=Js(0.0)):
                var.put('x', (((+var.get('s').get(var.get('i')))&Js(255)) if (var.get('k')==Js(8.0)) else var.get('intAt')(var.get('s'), var.get('i'))))
                if (var.get('x')<Js(0.0)):
                    if (var.get('s').callprop('charAt', var.get('i'))==Js('-')):
                        var.put('mi', Js(True))
                    continue
                var.put('mi', Js(False))
                if (var.get('sh')==Js(0.0)):
                    var.get(u"this").put((var.get(u"this").put('t',Js(var.get(u"this").get('t').to_number())+Js(1))-Js(1)), var.get('x'))
                else:
                    if ((var.get('sh')+var.get('k'))>var.get(u"this").get('DB')):
                        var.get(u"this").put((var.get(u"this").get('t')-Js(1.0)), ((var.get('x')&((Js(1.0)<<(var.get(u"this").get('DB')-var.get('sh')))-Js(1.0)))<<var.get('sh')), '|')
                        var.get(u"this").put((var.get(u"this").put('t',Js(var.get(u"this").get('t').to_number())+Js(1))-Js(1)), (var.get('x')>>(var.get(u"this").get('DB')-var.get('sh'))))
                    else:
                        var.get(u"this").put((var.get(u"this").get('t')-Js(1.0)), (var.get('x')<<var.get('sh')), '|')
                var.put('sh', var.get('k'), '+')
                if (var.get('sh')>=var.get(u"this").get('DB')):
                    var.put('sh', var.get(u"this").get('DB'), '-')
            if ((var.get('k')==Js(8.0)) and (((+var.get('s').get('0'))&Js(128))!=Js(0.0))):
                var.get(u"this").put('s', (-Js(1.0)))
                if (var.get('sh')>Js(0.0)):
                    var.get(u"this").put((var.get(u"this").get('t')-Js(1.0)), (((Js(1.0)<<(var.get(u"this").get('DB')-var.get('sh')))-Js(1.0))<<var.get('sh')), '|')
            var.get(u"this").callprop('clamp')
            if var.get('mi'):
                var.get('BigInteger').get('ZERO').callprop('subTo', var.get(u"this"), var.get(u"this"))
        PyJs_anonymous_85_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('fromString', PyJs_anonymous_85_)
        @Js
        def PyJs_anonymous_86_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['c'])
            var.put('c', (var.get(u"this").get('s')&var.get(u"this").get('DM')))
            while ((var.get(u"this").get('t')>Js(0.0)) and (var.get(u"this").get((var.get(u"this").get('t')-Js(1.0)))==var.get('c'))):
                var.get(u"this").put('t',Js(var.get(u"this").get('t').to_number())-Js(1))
        PyJs_anonymous_86_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('clamp', PyJs_anonymous_86_)
        @Js
        def PyJs_anonymous_87_(n, r, this, arguments, var=var):
            var = Scope({'n':n, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'n', 'r'])
            pass
            #for JS loop
            var.put('i', (var.get(u"this").get('t')-Js(1.0)))
            while (var.get('i')>=Js(0.0)):
                try:
                    var.get('r').put((var.get('i')+var.get('n')), var.get(u"this").get(var.get('i')))
                finally:
                        var.put('i',Js(var.get('i').to_number())-Js(1))
            #for JS loop
            var.put('i', (var.get('n')-Js(1.0)))
            while (var.get('i')>=Js(0.0)):
                try:
                    var.get('r').put(var.get('i'), Js(0.0))
                finally:
                        var.put('i',Js(var.get('i').to_number())-Js(1))
            var.get('r').put('t', (var.get(u"this").get('t')+var.get('n')))
            var.get('r').put('s', var.get(u"this").get('s'))
        PyJs_anonymous_87_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('dlShiftTo', PyJs_anonymous_87_)
        @Js
        def PyJs_anonymous_88_(n, r, this, arguments, var=var):
            var = Scope({'n':n, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'n', 'r'])
            #for JS loop
            var.put('i', var.get('n'))
            while (var.get('i')<var.get(u"this").get('t')):
                try:
                    var.get('r').put((var.get('i')-var.get('n')), var.get(u"this").get(var.get('i')))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            var.get('r').put('t', var.get('Math').callprop('max', (var.get(u"this").get('t')-var.get('n')), Js(0.0)))
            var.get('r').put('s', var.get(u"this").get('s'))
        PyJs_anonymous_88_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('drShiftTo', PyJs_anonymous_88_)
        @Js
        def PyJs_anonymous_89_(n, r, this, arguments, var=var):
            var = Scope({'n':n, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['c', 'r', 'ds', 'cbs', 'bm', 'bs', 'i', 'n'])
            var.put('bs', (var.get('n')%var.get(u"this").get('DB')))
            var.put('cbs', (var.get(u"this").get('DB')-var.get('bs')))
            var.put('bm', ((Js(1.0)<<var.get('cbs'))-Js(1.0)))
            var.put('ds', var.get('Math').callprop('floor', (var.get('n')/var.get(u"this").get('DB'))))
            var.put('c', ((var.get(u"this").get('s')<<var.get('bs'))&var.get(u"this").get('DM')))
            #for JS loop
            var.put('i', (var.get(u"this").get('t')-Js(1.0)))
            while (var.get('i')>=Js(0.0)):
                try:
                    var.get('r').put(((var.get('i')+var.get('ds'))+Js(1.0)), ((var.get(u"this").get(var.get('i'))>>var.get('cbs'))|var.get('c')))
                    var.put('c', ((var.get(u"this").get(var.get('i'))&var.get('bm'))<<var.get('bs')))
                finally:
                        var.put('i',Js(var.get('i').to_number())-Js(1))
            #for JS loop
            var.put('i', (var.get('ds')-Js(1.0)))
            while (var.get('i')>=Js(0.0)):
                try:
                    var.get('r').put(var.get('i'), Js(0.0))
                finally:
                        var.put('i',Js(var.get('i').to_number())-Js(1))
            var.get('r').put(var.get('ds'), var.get('c'))
            var.get('r').put('t', ((var.get(u"this").get('t')+var.get('ds'))+Js(1.0)))
            var.get('r').put('s', var.get(u"this").get('s'))
            var.get('r').callprop('clamp')
        PyJs_anonymous_89_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('lShiftTo', PyJs_anonymous_89_)
        @Js
        def PyJs_anonymous_90_(n, r, this, arguments, var=var):
            var = Scope({'n':n, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['r', 'ds', 'cbs', 'bs', 'bm', 'i', 'n'])
            var.get('r').put('s', var.get(u"this").get('s'))
            var.put('ds', var.get('Math').callprop('floor', (var.get('n')/var.get(u"this").get('DB'))))
            if (var.get('ds')>=var.get(u"this").get('t')):
                var.get('r').put('t', Js(0.0))
                return var.get('undefined')
            var.put('bs', (var.get('n')%var.get(u"this").get('DB')))
            var.put('cbs', (var.get(u"this").get('DB')-var.get('bs')))
            var.put('bm', ((Js(1.0)<<var.get('bs'))-Js(1.0)))
            var.get('r').put('0', (var.get(u"this").get(var.get('ds'))>>var.get('bs')))
            #for JS loop
            var.put('i', (var.get('ds')+Js(1.0)))
            while (var.get('i')<var.get(u"this").get('t')):
                try:
                    var.get('r').put(((var.get('i')-var.get('ds'))-Js(1.0)), ((var.get(u"this").get(var.get('i'))&var.get('bm'))<<var.get('cbs')), '|')
                    var.get('r').put((var.get('i')-var.get('ds')), (var.get(u"this").get(var.get('i'))>>var.get('bs')))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            if (var.get('bs')>Js(0.0)):
                var.get('r').put(((var.get(u"this").get('t')-var.get('ds'))-Js(1.0)), ((var.get(u"this").get('s')&var.get('bm'))<<var.get('cbs')), '|')
            var.get('r').put('t', (var.get(u"this").get('t')-var.get('ds')))
            var.get('r').callprop('clamp')
        PyJs_anonymous_90_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('rShiftTo', PyJs_anonymous_90_)
        @Js
        def PyJs_anonymous_91_(a, r, this, arguments, var=var):
            var = Scope({'a':a, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['m', 'a', 'r', 'c', 'i'])
            var.put('i', Js(0.0))
            var.put('c', Js(0.0))
            var.put('m', var.get('Math').callprop('min', var.get('a').get('t'), var.get(u"this").get('t')))
            while (var.get('i')<var.get('m')):
                var.put('c', (var.get(u"this").get(var.get('i'))-var.get('a').get(var.get('i'))), '+')
                var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), (var.get('c')&var.get(u"this").get('DM')))
                var.put('c', var.get(u"this").get('DB'), '>>')
            if (var.get('a').get('t')<var.get(u"this").get('t')):
                var.put('c', var.get('a').get('s'), '-')
                while (var.get('i')<var.get(u"this").get('t')):
                    var.put('c', var.get(u"this").get(var.get('i')), '+')
                    var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), (var.get('c')&var.get(u"this").get('DM')))
                    var.put('c', var.get(u"this").get('DB'), '>>')
                var.put('c', var.get(u"this").get('s'), '+')
            else:
                var.put('c', var.get(u"this").get('s'), '+')
                while (var.get('i')<var.get('a').get('t')):
                    var.put('c', var.get('a').get(var.get('i')), '-')
                    var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), (var.get('c')&var.get(u"this").get('DM')))
                    var.put('c', var.get(u"this").get('DB'), '>>')
                var.put('c', var.get('a').get('s'), '-')
            var.get('r').put('s', ((-Js(1.0)) if (var.get('c')<Js(0.0)) else Js(0.0)))
            if (var.get('c')<(-Js(1.0))):
                var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), (var.get(u"this").get('DV')+var.get('c')))
            else:
                if (var.get('c')>Js(0.0)):
                    var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), var.get('c'))
            var.get('r').put('t', var.get('i'))
            var.get('r').callprop('clamp')
        PyJs_anonymous_91_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('subTo', PyJs_anonymous_91_)
        @Js
        def PyJs_anonymous_92_(a, r, this, arguments, var=var):
            var = Scope({'a':a, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['x', 'a', 'r', 'y', 'i'])
            var.put('x', var.get(u"this").callprop('abs'))
            var.put('y', var.get('a').callprop('abs'))
            var.put('i', var.get('x').get('t'))
            var.get('r').put('t', (var.get('i')+var.get('y').get('t')))
            while (var.put('i',Js(var.get('i').to_number())-Js(1))>=Js(0.0)):
                var.get('r').put(var.get('i'), Js(0.0))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('y').get('t')):
                try:
                    var.get('r').put((var.get('i')+var.get('x').get('t')), var.get('x').callprop('am', Js(0.0), var.get('y').get(var.get('i')), var.get('r'), var.get('i'), Js(0.0), var.get('x').get('t')))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            var.get('r').put('s', Js(0.0))
            var.get('r').callprop('clamp')
            if (var.get(u"this").get('s')!=var.get('a').get('s')):
                var.get('BigInteger').get('ZERO').callprop('subTo', var.get('r'), var.get('r'))
        PyJs_anonymous_92_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('multiplyTo', PyJs_anonymous_92_)
        @Js
        def PyJs_anonymous_93_(r, this, arguments, var=var):
            var = Scope({'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'x', 'r', 'c'])
            var.put('x', var.get(u"this").callprop('abs'))
            var.put('i', var.get('r').put('t', (Js(2.0)*var.get('x').get('t'))))
            while (var.put('i',Js(var.get('i').to_number())-Js(1))>=Js(0.0)):
                var.get('r').put(var.get('i'), Js(0.0))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<(var.get('x').get('t')-Js(1.0))):
                try:
                    var.put('c', var.get('x').callprop('am', var.get('i'), var.get('x').get(var.get('i')), var.get('r'), (Js(2.0)*var.get('i')), Js(0.0), Js(1.0)))
                    if (var.get('r').put((var.get('i')+var.get('x').get('t')), var.get('x').callprop('am', (var.get('i')+Js(1.0)), (Js(2.0)*var.get('x').get(var.get('i'))), var.get('r'), ((Js(2.0)*var.get('i'))+Js(1.0)), var.get('c'), ((var.get('x').get('t')-var.get('i'))-Js(1.0))), '+')>=var.get('x').get('DV')):
                        var.get('r').put((var.get('i')+var.get('x').get('t')), var.get('x').get('DV'), '-')
                        var.get('r').put(((var.get('i')+var.get('x').get('t'))+Js(1.0)), Js(1.0))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            if (var.get('r').get('t')>Js(0.0)):
                var.get('r').put((var.get('r').get('t')-Js(1.0)), var.get('x').callprop('am', var.get('i'), var.get('x').get(var.get('i')), var.get('r'), (Js(2.0)*var.get('i')), Js(0.0), Js(1.0)), '+')
            var.get('r').put('s', Js(0.0))
            var.get('r').callprop('clamp')
        PyJs_anonymous_93_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('squareTo', PyJs_anonymous_93_)
        @Js
        def PyJs_anonymous_94_(m, q, r, this, arguments, var=var):
            var = Scope({'m':m, 'q':q, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['qd', 'pt', 'j', 'y0', 'd2', 'ys', 'y', 'd1', 'e', 'nsh', 'yt', 't', 'i', 'ts', 'q', 'm', 'r', 'pm', 'ms'])
            var.put('pm', var.get('m').callprop('abs'))
            if (var.get('pm').get('t')<=Js(0.0)):
                return var.get('undefined')
            var.put('pt', var.get(u"this").callprop('abs'))
            if (var.get('pt').get('t')<var.get('pm').get('t')):
                if (var.get('q')!=var.get(u"null")):
                    var.get('q').callprop('fromInt', Js(0.0))
                if (var.get('r')!=var.get(u"null")):
                    var.get(u"this").callprop('copyTo', var.get('r'))
                return var.get('undefined')
            if (var.get('r')==var.get(u"null")):
                var.put('r', var.get('nbi')())
            var.put('y', var.get('nbi')())
            var.put('ts', var.get(u"this").get('s'))
            var.put('ms', var.get('m').get('s'))
            var.put('nsh', (var.get(u"this").get('DB')-var.get('nbits')(var.get('pm').get((var.get('pm').get('t')-Js(1.0))))))
            if (var.get('nsh')>Js(0.0)):
                var.get('pm').callprop('lShiftTo', var.get('nsh'), var.get('y'))
                var.get('pt').callprop('lShiftTo', var.get('nsh'), var.get('r'))
            else:
                var.get('pm').callprop('copyTo', var.get('y'))
                var.get('pt').callprop('copyTo', var.get('r'))
            var.put('ys', var.get('y').get('t'))
            var.put('y0', var.get('y').get((var.get('ys')-Js(1.0))))
            if (var.get('y0')==Js(0.0)):
                return var.get('undefined')
            var.put('yt', ((var.get('y0')*(Js(1.0)<<var.get(u"this").get('F1')))+((var.get('y').get((var.get('ys')-Js(2.0)))>>var.get(u"this").get('F2')) if (var.get('ys')>Js(1.0)) else Js(0.0))))
            var.put('d1', (var.get(u"this").get('FV')/var.get('yt')))
            var.put('d2', ((Js(1.0)<<var.get(u"this").get('F1'))/var.get('yt')))
            var.put('e', (Js(1.0)<<var.get(u"this").get('F2')))
            var.put('i', var.get('r').get('t'))
            var.put('j', (var.get('i')-var.get('ys')))
            var.put('t', (var.get('nbi')() if (var.get('q')==var.get(u"null")) else var.get('q')))
            var.get('y').callprop('dlShiftTo', var.get('j'), var.get('t'))
            if (var.get('r').callprop('compareTo', var.get('t'))>=Js(0.0)):
                var.get('r').put((var.get('r').put('t',Js(var.get('r').get('t').to_number())+Js(1))-Js(1)), Js(1.0))
                var.get('r').callprop('subTo', var.get('t'), var.get('r'))
            var.get('BigInteger').get('ONE').callprop('dlShiftTo', var.get('ys'), var.get('t'))
            var.get('t').callprop('subTo', var.get('y'), var.get('y'))
            while (var.get('y').get('t')<var.get('ys')):
                var.get('y').put((var.get('y').put('t',Js(var.get('y').get('t').to_number())+Js(1))-Js(1)), Js(0.0))
            while (var.put('j',Js(var.get('j').to_number())-Js(1))>=Js(0.0)):
                var.put('qd', (var.get(u"this").get('DM') if (var.get('r').get(var.put('i',Js(var.get('i').to_number())-Js(1)))==var.get('y0')) else var.get('Math').callprop('floor', ((var.get('r').get(var.get('i'))*var.get('d1'))+((var.get('r').get((var.get('i')-Js(1.0)))+var.get('e'))*var.get('d2'))))))
                if (var.get('r').put(var.get('i'), var.get('y').callprop('am', Js(0.0), var.get('qd'), var.get('r'), var.get('j'), Js(0.0), var.get('ys')), '+')<var.get('qd')):
                    var.get('y').callprop('dlShiftTo', var.get('j'), var.get('t'))
                    var.get('r').callprop('subTo', var.get('t'), var.get('r'))
                    while (var.get('r').get(var.get('i'))<var.put('qd',Js(var.get('qd').to_number())-Js(1))):
                        var.get('r').callprop('subTo', var.get('t'), var.get('r'))
            if (var.get('q')!=var.get(u"null")):
                var.get('r').callprop('drShiftTo', var.get('ys'), var.get('q'))
                if (var.get('ts')!=var.get('ms')):
                    var.get('BigInteger').get('ZERO').callprop('subTo', var.get('q'), var.get('q'))
            var.get('r').put('t', var.get('ys'))
            var.get('r').callprop('clamp')
            if (var.get('nsh')>Js(0.0)):
                var.get('r').callprop('rShiftTo', var.get('nsh'), var.get('r'))
            if (var.get('ts')<Js(0.0)):
                var.get('BigInteger').get('ZERO').callprop('subTo', var.get('r'), var.get('r'))
        PyJs_anonymous_94_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('divRemTo', PyJs_anonymous_94_)
        @Js
        def PyJs_anonymous_95_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x'])
            if (var.get(u"this").get('t')<Js(1.0)):
                return Js(0.0)
            var.put('x', var.get(u"this").get('0'))
            if ((var.get('x')&Js(1.0))==Js(0.0)):
                return Js(0.0)
            var.put('y', (var.get('x')&Js(3.0)))
            var.put('y', ((var.get('y')*(Js(2.0)-((var.get('x')&Js(15))*var.get('y'))))&Js(15)))
            var.put('y', ((var.get('y')*(Js(2.0)-((var.get('x')&Js(255))*var.get('y'))))&Js(255)))
            var.put('y', ((var.get('y')*(Js(2.0)-(((var.get('x')&Js(65535))*var.get('y'))&Js(65535))))&Js(65535)))
            var.put('y', ((var.get('y')*(Js(2.0)-((var.get('x')*var.get('y'))%var.get(u"this").get('DV'))))%var.get(u"this").get('DV')))
            return ((var.get(u"this").get('DV')-var.get('y')) if (var.get('y')>Js(0.0)) else (-var.get('y')))
        PyJs_anonymous_95_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('invDigit', PyJs_anonymous_95_)
        @Js
        def PyJs_anonymous_96_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return (((var.get(u"this").get('0')&Js(1.0)) if (var.get(u"this").get('t')>Js(0.0)) else var.get(u"this").get('s'))==Js(0.0))
        PyJs_anonymous_96_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('isEven', PyJs_anonymous_96_)
        @Js
        def PyJs_anonymous_97_(e, z, this, arguments, var=var):
            var = Scope({'e':e, 'z':z, 'this':this, 'arguments':arguments}, var)
            var.registers(['g', 'r2', 'r', 't', 'z', 'i', 'e'])
            if ((var.get('e')>Js(4294967295)) or (var.get('e')<Js(1.0))):
                return var.get('BigInteger').get('ONE')
            var.put('r', var.get('nbi')())
            var.put('r2', var.get('nbi')())
            var.put('g', var.get('z').callprop('convert', var.get(u"this")))
            var.put('i', (var.get('nbits')(var.get('e'))-Js(1.0)))
            var.get('g').callprop('copyTo', var.get('r'))
            while (var.put('i',Js(var.get('i').to_number())-Js(1))>=Js(0.0)):
                var.get('z').callprop('sqrTo', var.get('r'), var.get('r2'))
                if ((var.get('e')&(Js(1.0)<<var.get('i')))>Js(0.0)):
                    var.get('z').callprop('mulTo', var.get('r2'), var.get('g'), var.get('r'))
                else:
                    var.put('t', var.get('r'))
                    var.put('r', var.get('r2'))
                    var.put('r2', var.get('t'))
            return var.get('z').callprop('revert', var.get('r'))
        PyJs_anonymous_97_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('exp', PyJs_anonymous_97_)
        @Js
        def PyJs_anonymous_98_(r, this, arguments, var=var):
            var = Scope({'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['r'])
            return var.get('Math').callprop('floor', ((var.get('Math').get('LN2')*var.get(u"this").get('DB'))/var.get('Math').callprop('log', var.get('r'))))
        PyJs_anonymous_98_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('chunkSize', PyJs_anonymous_98_)
        @Js
        def PyJs_anonymous_99_(b, this, arguments, var=var):
            var = Scope({'b':b, 'this':this, 'arguments':arguments}, var)
            var.registers(['b', 'd', 'z', 'a', 'r', 'y', 'cs'])
            if (var.get('b')==var.get(u"null")):
                var.put('b', Js(10.0))
            if (((var.get(u"this").callprop('signum')==Js(0.0)) or (var.get('b')<Js(2.0))) or (var.get('b')>Js(36.0))):
                return Js('0')
            var.put('cs', var.get(u"this").callprop('chunkSize', var.get('b')))
            var.put('a', var.get('Math').callprop('pow', var.get('b'), var.get('cs')))
            var.put('d', var.get('nbv')(var.get('a')))
            var.put('y', var.get('nbi')())
            var.put('z', var.get('nbi')())
            var.put('r', Js(''))
            var.get(u"this").callprop('divRemTo', var.get('d'), var.get('y'), var.get('z'))
            while (var.get('y').callprop('signum')>Js(0.0)):
                var.put('r', ((var.get('a')+var.get('z').callprop('intValue')).callprop('toString', var.get('b')).callprop('substr', Js(1.0))+var.get('r')))
                var.get('y').callprop('divRemTo', var.get('d'), var.get('y'), var.get('z'))
            return (var.get('z').callprop('intValue').callprop('toString', var.get('b'))+var.get('r'))
        PyJs_anonymous_99_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('toRadix', PyJs_anonymous_99_)
        @Js
        def PyJs_anonymous_100_(s, b, this, arguments, var=var):
            var = Scope({'s':s, 'b':b, 'this':this, 'arguments':arguments}, var)
            var.registers(['x', 'b', 's', 'w', 'd', 'mi', 'i', 'j', 'cs'])
            var.get(u"this").callprop('fromInt', Js(0.0))
            if (var.get('b')==var.get(u"null")):
                var.put('b', Js(10.0))
            var.put('cs', var.get(u"this").callprop('chunkSize', var.get('b')))
            var.put('d', var.get('Math').callprop('pow', var.get('b'), var.get('cs')))
            var.put('mi', Js(False))
            var.put('j', Js(0.0))
            var.put('w', Js(0.0))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('s').get('length')):
                try:
                    var.put('x', var.get('intAt')(var.get('s'), var.get('i')))
                    if (var.get('x')<Js(0.0)):
                        if ((var.get('s').callprop('charAt', var.get('i'))==Js('-')) and (var.get(u"this").callprop('signum')==Js(0.0))):
                            var.put('mi', Js(True))
                        continue
                    var.put('w', ((var.get('b')*var.get('w'))+var.get('x')))
                    if (var.put('j',Js(var.get('j').to_number())+Js(1))>=var.get('cs')):
                        var.get(u"this").callprop('dMultiply', var.get('d'))
                        var.get(u"this").callprop('dAddOffset', var.get('w'), Js(0.0))
                        var.put('j', Js(0.0))
                        var.put('w', Js(0.0))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            if (var.get('j')>Js(0.0)):
                var.get(u"this").callprop('dMultiply', var.get('Math').callprop('pow', var.get('b'), var.get('j')))
                var.get(u"this").callprop('dAddOffset', var.get('w'), Js(0.0))
            if var.get('mi'):
                var.get('BigInteger').get('ZERO').callprop('subTo', var.get(u"this"), var.get(u"this"))
        PyJs_anonymous_100_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('fromRadix', PyJs_anonymous_100_)
        @Js
        def PyJs_anonymous_101_(a, b, c, this, arguments, var=var):
            var = Scope({'a':a, 'b':b, 'c':c, 'this':this, 'arguments':arguments}, var)
            var.registers(['x', 'b', 'a', 'c', 't'])
            if (Js('number')==var.get('b',throw=False).typeof()):
                if (var.get('a')<Js(2.0)):
                    var.get(u"this").callprop('fromInt', Js(1.0))
                else:
                    var.get(u"this").callprop('fromNumber', var.get('a'), var.get('c'))
                    if var.get(u"this").callprop('testBit', (var.get('a')-Js(1.0))).neg():
                        var.get(u"this").callprop('bitwiseTo', var.get('BigInteger').get('ONE').callprop('shiftLeft', (var.get('a')-Js(1.0))), var.get('op_or'), var.get(u"this"))
                    if var.get(u"this").callprop('isEven'):
                        var.get(u"this").callprop('dAddOffset', Js(1.0), Js(0.0))
                    while var.get(u"this").callprop('isProbablePrime', var.get('b')).neg():
                        var.get(u"this").callprop('dAddOffset', Js(2.0), Js(0.0))
                        if (var.get(u"this").callprop('bitLength')>var.get('a')):
                            var.get(u"this").callprop('subTo', var.get('BigInteger').get('ONE').callprop('shiftLeft', (var.get('a')-Js(1.0))), var.get(u"this"))
            else:
                var.put('x', Js([]))
                var.put('t', (var.get('a')&Js(7.0)))
                var.get('x').put('length', ((var.get('a')>>Js(3.0))+Js(1.0)))
                var.get('b').callprop('nextBytes', var.get('x'))
                if (var.get('t')>Js(0.0)):
                    var.get('x').put('0', ((Js(1.0)<<var.get('t'))-Js(1.0)), '&')
                else:
                    var.get('x').put('0', Js(0.0))
                var.get(u"this").callprop('fromString', var.get('x'), Js(256.0))
        PyJs_anonymous_101_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('fromNumber', PyJs_anonymous_101_)
        @Js
        def PyJs_anonymous_102_(a, op, r, this, arguments, var=var):
            var = Scope({'a':a, 'op':op, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['m', 'op', 'a', 'r', 'i', 'f'])
            pass
            pass
            var.put('m', var.get('Math').callprop('min', var.get('a').get('t'), var.get(u"this").get('t')))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('m')):
                try:
                    var.get('r').put(var.get('i'), var.get('op')(var.get(u"this").get(var.get('i')), var.get('a').get(var.get('i'))))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            if (var.get('a').get('t')<var.get(u"this").get('t')):
                var.put('f', (var.get('a').get('s')&var.get(u"this").get('DM')))
                #for JS loop
                var.put('i', var.get('m'))
                while (var.get('i')<var.get(u"this").get('t')):
                    try:
                        var.get('r').put(var.get('i'), var.get('op')(var.get(u"this").get(var.get('i')), var.get('f')))
                    finally:
                            var.put('i',Js(var.get('i').to_number())+Js(1))
                var.get('r').put('t', var.get(u"this").get('t'))
            else:
                var.put('f', (var.get(u"this").get('s')&var.get(u"this").get('DM')))
                #for JS loop
                var.put('i', var.get('m'))
                while (var.get('i')<var.get('a').get('t')):
                    try:
                        var.get('r').put(var.get('i'), var.get('op')(var.get('f'), var.get('a').get(var.get('i'))))
                    finally:
                            var.put('i',Js(var.get('i').to_number())+Js(1))
                var.get('r').put('t', var.get('a').get('t'))
            var.get('r').put('s', var.get('op')(var.get(u"this").get('s'), var.get('a').get('s')))
            var.get('r').callprop('clamp')
        PyJs_anonymous_102_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('bitwiseTo', PyJs_anonymous_102_)
        @Js
        def PyJs_anonymous_103_(n, op, this, arguments, var=var):
            var = Scope({'n':n, 'op':op, 'this':this, 'arguments':arguments}, var)
            var.registers(['op', 'n', 'r'])
            var.put('r', var.get('BigInteger').get('ONE').callprop('shiftLeft', var.get('n')))
            var.get(u"this").callprop('bitwiseTo', var.get('r'), var.get('op'), var.get('r'))
            return var.get('r')
        PyJs_anonymous_103_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('changeBit', PyJs_anonymous_103_)
        @Js
        def PyJs_anonymous_104_(a, r, this, arguments, var=var):
            var = Scope({'a':a, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['m', 'a', 'r', 'c', 'i'])
            var.put('i', Js(0.0))
            var.put('c', Js(0.0))
            var.put('m', var.get('Math').callprop('min', var.get('a').get('t'), var.get(u"this").get('t')))
            while (var.get('i')<var.get('m')):
                var.put('c', (var.get(u"this").get(var.get('i'))+var.get('a').get(var.get('i'))), '+')
                var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), (var.get('c')&var.get(u"this").get('DM')))
                var.put('c', var.get(u"this").get('DB'), '>>')
            if (var.get('a').get('t')<var.get(u"this").get('t')):
                var.put('c', var.get('a').get('s'), '+')
                while (var.get('i')<var.get(u"this").get('t')):
                    var.put('c', var.get(u"this").get(var.get('i')), '+')
                    var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), (var.get('c')&var.get(u"this").get('DM')))
                    var.put('c', var.get(u"this").get('DB'), '>>')
                var.put('c', var.get(u"this").get('s'), '+')
            else:
                var.put('c', var.get(u"this").get('s'), '+')
                while (var.get('i')<var.get('a').get('t')):
                    var.put('c', var.get('a').get(var.get('i')), '+')
                    var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), (var.get('c')&var.get(u"this").get('DM')))
                    var.put('c', var.get(u"this").get('DB'), '>>')
                var.put('c', var.get('a').get('s'), '+')
            var.get('r').put('s', ((-Js(1.0)) if (var.get('c')<Js(0.0)) else Js(0.0)))
            if (var.get('c')>Js(0.0)):
                var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), var.get('c'))
            else:
                if (var.get('c')<(-Js(1.0))):
                    var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), (var.get(u"this").get('DV')+var.get('c')))
            var.get('r').put('t', var.get('i'))
            var.get('r').callprop('clamp')
        PyJs_anonymous_104_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('addTo', PyJs_anonymous_104_)
        @Js
        def PyJs_anonymous_105_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['n'])
            var.get(u"this").put(var.get(u"this").get('t'), var.get(u"this").callprop('am', Js(0.0), (var.get('n')-Js(1.0)), var.get(u"this"), Js(0.0), Js(0.0), var.get(u"this").get('t')))
            var.get(u"this").put('t',Js(var.get(u"this").get('t').to_number())+Js(1))
            var.get(u"this").callprop('clamp')
        PyJs_anonymous_105_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('dMultiply', PyJs_anonymous_105_)
        @Js
        def PyJs_anonymous_106_(n, w, this, arguments, var=var):
            var = Scope({'n':n, 'w':w, 'this':this, 'arguments':arguments}, var)
            var.registers(['n', 'w'])
            if (var.get('n')==Js(0.0)):
                return var.get('undefined')
            while (var.get(u"this").get('t')<=var.get('w')):
                var.get(u"this").put((var.get(u"this").put('t',Js(var.get(u"this").get('t').to_number())+Js(1))-Js(1)), Js(0.0))
            var.get(u"this").put(var.get('w'), var.get('n'), '+')
            while (var.get(u"this").get(var.get('w'))>=var.get(u"this").get('DV')):
                var.get(u"this").put(var.get('w'), var.get(u"this").get('DV'), '-')
                if (var.put('w',Js(var.get('w').to_number())+Js(1))>=var.get(u"this").get('t')):
                    var.get(u"this").put((var.get(u"this").put('t',Js(var.get(u"this").get('t').to_number())+Js(1))-Js(1)), Js(0.0))
                var.get(u"this").put(var.get('w'),Js(var.get(u"this").get(var.get('w')).to_number())+Js(1))
        PyJs_anonymous_106_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('dAddOffset', PyJs_anonymous_106_)
        @Js
        def PyJs_anonymous_107_(a, n, r, this, arguments, var=var):
            var = Scope({'a':a, 'n':n, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'r', 'i', 'j', 'n'])
            var.put('i', var.get('Math').callprop('min', (var.get(u"this").get('t')+var.get('a').get('t')), var.get('n')))
            var.get('r').put('s', Js(0.0))
            var.get('r').put('t', var.get('i'))
            while (var.get('i')>Js(0.0)):
                var.get('r').put(var.put('i',Js(var.get('i').to_number())-Js(1)), Js(0.0))
            #for JS loop
            var.put('j', (var.get('r').get('t')-var.get(u"this").get('t')))
            while (var.get('i')<var.get('j')):
                try:
                    var.get('r').put((var.get('i')+var.get(u"this").get('t')), var.get(u"this").callprop('am', Js(0.0), var.get('a').get(var.get('i')), var.get('r'), var.get('i'), Js(0.0), var.get(u"this").get('t')))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            #for JS loop
            var.put('j', var.get('Math').callprop('min', var.get('a').get('t'), var.get('n')))
            while (var.get('i')<var.get('j')):
                try:
                    var.get(u"this").callprop('am', Js(0.0), var.get('a').get(var.get('i')), var.get('r'), var.get('i'), Js(0.0), (var.get('n')-var.get('i')))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            var.get('r').callprop('clamp')
        PyJs_anonymous_107_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('multiplyLowerTo', PyJs_anonymous_107_)
        @Js
        def PyJs_anonymous_108_(a, n, r, this, arguments, var=var):
            var = Scope({'a':a, 'n':n, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'n', 'a', 'r'])
            var.put('n',Js(var.get('n').to_number())-Js(1))
            var.put('i', var.get('r').put('t', ((var.get(u"this").get('t')+var.get('a').get('t'))-var.get('n'))))
            var.get('r').put('s', Js(0.0))
            while (var.put('i',Js(var.get('i').to_number())-Js(1))>=Js(0.0)):
                var.get('r').put(var.get('i'), Js(0.0))
            #for JS loop
            var.put('i', var.get('Math').callprop('max', (var.get('n')-var.get(u"this").get('t')), Js(0.0)))
            while (var.get('i')<var.get('a').get('t')):
                try:
                    var.get('r').put(((var.get(u"this").get('t')+var.get('i'))-var.get('n')), var.get(u"this").callprop('am', (var.get('n')-var.get('i')), var.get('a').get(var.get('i')), var.get('r'), Js(0.0), Js(0.0), ((var.get(u"this").get('t')+var.get('i'))-var.get('n'))))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            var.get('r').callprop('clamp')
            var.get('r').callprop('drShiftTo', Js(1.0), var.get('r'))
        PyJs_anonymous_108_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('multiplyUpperTo', PyJs_anonymous_108_)
        @Js
        def PyJs_anonymous_109_(n, this, arguments, var=var):
            var = Scope({'n':n, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'n', 'r', 'd'])
            if (var.get('n')<=Js(0.0)):
                return Js(0.0)
            var.put('d', (var.get(u"this").get('DV')%var.get('n')))
            var.put('r', ((var.get('n')-Js(1.0)) if (var.get(u"this").get('s')<Js(0.0)) else Js(0.0)))
            if (var.get(u"this").get('t')>Js(0.0)):
                if (var.get('d')==Js(0.0)):
                    var.put('r', (var.get(u"this").get('0')%var.get('n')))
                else:
                    #for JS loop
                    var.put('i', (var.get(u"this").get('t')-Js(1.0)))
                    while (var.get('i')>=Js(0.0)):
                        try:
                            var.put('r', (((var.get('d')*var.get('r'))+var.get(u"this").get(var.get('i')))%var.get('n')))
                        finally:
                                var.put('i',Js(var.get('i').to_number())-Js(1))
            return var.get('r')
        PyJs_anonymous_109_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('modInt', PyJs_anonymous_109_)
        @Js
        def PyJs_anonymous_110_(t, this, arguments, var=var):
            var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
            var.registers(['k', 'a', 'r', 't', 'y', 'i', 'j', 'n1'])
            var.put('n1', var.get(u"this").callprop('subtract', var.get('BigInteger').get('ONE')))
            var.put('k', var.get('n1').callprop('getLowestSetBit'))
            if (var.get('k')<=Js(0.0)):
                return Js(False)
            var.put('r', var.get('n1').callprop('shiftRight', var.get('k')))
            var.put('t', ((var.get('t')+Js(1.0))>>Js(1.0)))
            if (var.get('t')>var.get('lowprimes').get('length')):
                var.put('t', var.get('lowprimes').get('length'))
            var.put('a', var.get('nbi')())
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('t')):
                try:
                    var.get('a').callprop('fromInt', var.get('lowprimes').get(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('lowprimes').get('length')))))
                    var.put('y', var.get('a').callprop('modPow', var.get('r'), var.get(u"this")))
                    if ((var.get('y').callprop('compareTo', var.get('BigInteger').get('ONE'))!=Js(0.0)) and (var.get('y').callprop('compareTo', var.get('n1'))!=Js(0.0))):
                        var.put('j', Js(1.0))
                        while (((var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))<var.get('k')) and (var.get('y').callprop('compareTo', var.get('n1'))!=Js(0.0))):
                            var.put('y', var.get('y').callprop('modPowInt', Js(2.0), var.get(u"this")))
                            if (var.get('y').callprop('compareTo', var.get('BigInteger').get('ONE'))==Js(0.0)):
                                return Js(False)
                        if (var.get('y').callprop('compareTo', var.get('n1'))!=Js(0.0)):
                            return Js(False)
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            return Js(True)
        PyJs_anonymous_110_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('millerRabin', PyJs_anonymous_110_)
        @Js
        def PyJs_anonymous_111_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['r'])
            var.put('r', var.get('nbi')())
            var.get(u"this").callprop('squareTo', var.get('r'))
            return var.get('r')
        PyJs_anonymous_111_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('square', PyJs_anonymous_111_)
        @Js
        def PyJs_anonymous_112_(a, callback, this, arguments, var=var):
            var = Scope({'a':a, 'callback':callback, 'this':this, 'arguments':arguments}, var)
            var.registers(['x', 'g', 'gcda1', 'callback', 'a', 't', 'y', 'i'])
            var.put('x', (var.get(u"this").callprop('negate') if (var.get(u"this").get('s')<Js(0.0)) else var.get(u"this").callprop('clone')))
            var.put('y', (var.get('a').callprop('negate') if (var.get('a').get('s')<Js(0.0)) else var.get('a').callprop('clone')))
            if (var.get('x').callprop('compareTo', var.get('y'))<Js(0.0)):
                var.put('t', var.get('x'))
                var.put('x', var.get('y'))
                var.put('y', var.get('t'))
            var.put('i', var.get('x').callprop('getLowestSetBit'))
            var.put('g', var.get('y').callprop('getLowestSetBit'))
            if (var.get('g')<Js(0.0)):
                var.get('callback')(var.get('x'))
                return var.get('undefined')
            if (var.get('i')<var.get('g')):
                var.put('g', var.get('i'))
            if (var.get('g')>Js(0.0)):
                var.get('x').callprop('rShiftTo', var.get('g'), var.get('x'))
                var.get('y').callprop('rShiftTo', var.get('g'), var.get('y'))
            @Js
            def PyJs_anonymous_113_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments}, var)
                var.registers([])
                if (var.put('i', var.get('x').callprop('getLowestSetBit'))>Js(0.0)):
                    var.get('x').callprop('rShiftTo', var.get('i'), var.get('x'))
                if (var.put('i', var.get('y').callprop('getLowestSetBit'))>Js(0.0)):
                    var.get('y').callprop('rShiftTo', var.get('i'), var.get('y'))
                if (var.get('x').callprop('compareTo', var.get('y'))>=Js(0.0)):
                    var.get('x').callprop('subTo', var.get('y'), var.get('x'))
                    var.get('x').callprop('rShiftTo', Js(1.0), var.get('x'))
                else:
                    var.get('y').callprop('subTo', var.get('x'), var.get('y'))
                    var.get('y').callprop('rShiftTo', Js(1.0), var.get('y'))
                if (var.get('x').callprop('signum')>Js(0.0)).neg():
                    if (var.get('g')>Js(0.0)):
                        var.get('y').callprop('lShiftTo', var.get('g'), var.get('y'))
                    @Js
                    def PyJs_anonymous_114_(this, arguments, var=var):
                        var = Scope({'this':this, 'arguments':arguments}, var)
                        var.registers([])
                        var.get('callback')(var.get('y'))
                    PyJs_anonymous_114_._set_name('anonymous')
                    var.get('setTimeout')(PyJs_anonymous_114_, Js(0.0))
                else:
                    var.get('setTimeout')(var.get('gcda1'), Js(0.0))
            PyJs_anonymous_113_._set_name('anonymous')
            var.put('gcda1', PyJs_anonymous_113_)
            var.get('setTimeout')(var.get('gcda1'), Js(10.0))
        PyJs_anonymous_112_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('gcda', PyJs_anonymous_112_)
        @Js
        def PyJs_anonymous_115_(a, b, c, callback, this, arguments, var=var):
            var = Scope({'a':a, 'b':b, 'c':c, 'callback':callback, 'this':this, 'arguments':arguments}, var)
            var.registers(['x', 'b', 'callback', 'a', 'c', 't', 'bnpfn1_1', 'bnp_1'])
            if (Js('number')==var.get('b',throw=False).typeof()):
                if (var.get('a')<Js(2.0)):
                    var.get(u"this").callprop('fromInt', Js(1.0))
                else:
                    var.get(u"this").callprop('fromNumber', var.get('a'), var.get('c'))
                    if var.get(u"this").callprop('testBit', (var.get('a')-Js(1.0))).neg():
                        var.get(u"this").callprop('bitwiseTo', var.get('BigInteger').get('ONE').callprop('shiftLeft', (var.get('a')-Js(1.0))), var.get('op_or'), var.get(u"this"))
                    if var.get(u"this").callprop('isEven'):
                        var.get(u"this").callprop('dAddOffset', Js(1.0), Js(0.0))
                    var.put('bnp_1', var.get(u"this"))
                    @Js
                    def PyJs_anonymous_116_(this, arguments, var=var):
                        var = Scope({'this':this, 'arguments':arguments}, var)
                        var.registers([])
                        var.get('bnp_1').callprop('dAddOffset', Js(2.0), Js(0.0))
                        if (var.get('bnp_1').callprop('bitLength')>var.get('a')):
                            var.get('bnp_1').callprop('subTo', var.get('BigInteger').get('ONE').callprop('shiftLeft', (var.get('a')-Js(1.0))), var.get('bnp_1'))
                        if var.get('bnp_1').callprop('isProbablePrime', var.get('b')):
                            @Js
                            def PyJs_anonymous_117_(this, arguments, var=var):
                                var = Scope({'this':this, 'arguments':arguments}, var)
                                var.registers([])
                                var.get('callback')()
                            PyJs_anonymous_117_._set_name('anonymous')
                            var.get('setTimeout')(PyJs_anonymous_117_, Js(0.0))
                        else:
                            var.get('setTimeout')(var.get('bnpfn1_1'), Js(0.0))
                    PyJs_anonymous_116_._set_name('anonymous')
                    var.put('bnpfn1_1', PyJs_anonymous_116_)
                    var.get('setTimeout')(var.get('bnpfn1_1'), Js(0.0))
            else:
                var.put('x', Js([]))
                var.put('t', (var.get('a')&Js(7.0)))
                var.get('x').put('length', ((var.get('a')>>Js(3.0))+Js(1.0)))
                var.get('b').callprop('nextBytes', var.get('x'))
                if (var.get('t')>Js(0.0)):
                    var.get('x').put('0', ((Js(1.0)<<var.get('t'))-Js(1.0)), '&')
                else:
                    var.get('x').put('0', Js(0.0))
                var.get(u"this").callprop('fromString', var.get('x'), Js(256.0))
        PyJs_anonymous_115_._set_name('anonymous')
        var.get('BigInteger').get('prototype').put('fromNumberAsync', PyJs_anonymous_115_)
        return var.get('BigInteger')
    PyJs_anonymous_42_._set_name('anonymous')
    var.put('BigInteger', PyJs_anonymous_42_())
    @Js
    def PyJs_anonymous_118_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['NullExp'])
        @Js
        def PyJsHoisted_NullExp_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            pass
        PyJsHoisted_NullExp_.func_name = 'NullExp'
        var.put('NullExp', PyJsHoisted_NullExp_)
        pass
        @Js
        def PyJs_anonymous_119_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x'])
            return var.get('x')
        PyJs_anonymous_119_._set_name('anonymous')
        var.get('NullExp').get('prototype').put('convert', PyJs_anonymous_119_)
        @Js
        def PyJs_anonymous_120_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x'])
            return var.get('x')
        PyJs_anonymous_120_._set_name('anonymous')
        var.get('NullExp').get('prototype').put('revert', PyJs_anonymous_120_)
        @Js
        def PyJs_anonymous_121_(x, y, r, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x', 'r'])
            var.get('x').callprop('multiplyTo', var.get('y'), var.get('r'))
        PyJs_anonymous_121_._set_name('anonymous')
        var.get('NullExp').get('prototype').put('mulTo', PyJs_anonymous_121_)
        @Js
        def PyJs_anonymous_122_(x, r, this, arguments, var=var):
            var = Scope({'x':x, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['x', 'r'])
            var.get('x').callprop('squareTo', var.get('r'))
        PyJs_anonymous_122_._set_name('anonymous')
        var.get('NullExp').get('prototype').put('sqrTo', PyJs_anonymous_122_)
        return var.get('NullExp')
    PyJs_anonymous_118_._set_name('anonymous')
    var.put('NullExp', PyJs_anonymous_118_())
    @Js
    def PyJs_anonymous_123_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['Classic'])
        @Js
        def PyJsHoisted_Classic_(m, this, arguments, var=var):
            var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['m'])
            var.get(u"this").put('m', var.get('m'))
        PyJsHoisted_Classic_.func_name = 'Classic'
        var.put('Classic', PyJsHoisted_Classic_)
        pass
        @Js
        def PyJs_anonymous_124_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x'])
            if ((var.get('x').get('s')<Js(0.0)) or (var.get('x').callprop('compareTo', var.get(u"this").get('m'))>=Js(0.0))):
                return var.get('x').callprop('mod', var.get(u"this").get('m'))
            else:
                return var.get('x')
        PyJs_anonymous_124_._set_name('anonymous')
        var.get('Classic').get('prototype').put('convert', PyJs_anonymous_124_)
        @Js
        def PyJs_anonymous_125_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x'])
            return var.get('x')
        PyJs_anonymous_125_._set_name('anonymous')
        var.get('Classic').get('prototype').put('revert', PyJs_anonymous_125_)
        @Js
        def PyJs_anonymous_126_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x'])
            var.get('x').callprop('divRemTo', var.get(u"this").get('m'), var.get(u"null"), var.get('x'))
        PyJs_anonymous_126_._set_name('anonymous')
        var.get('Classic').get('prototype').put('reduce', PyJs_anonymous_126_)
        @Js
        def PyJs_anonymous_127_(x, y, r, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x', 'r'])
            var.get('x').callprop('multiplyTo', var.get('y'), var.get('r'))
            var.get(u"this").callprop('reduce', var.get('r'))
        PyJs_anonymous_127_._set_name('anonymous')
        var.get('Classic').get('prototype').put('mulTo', PyJs_anonymous_127_)
        @Js
        def PyJs_anonymous_128_(x, r, this, arguments, var=var):
            var = Scope({'x':x, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['x', 'r'])
            var.get('x').callprop('squareTo', var.get('r'))
            var.get(u"this").callprop('reduce', var.get('r'))
        PyJs_anonymous_128_._set_name('anonymous')
        var.get('Classic').get('prototype').put('sqrTo', PyJs_anonymous_128_)
        return var.get('Classic')
    PyJs_anonymous_123_._set_name('anonymous')
    var.put('Classic', PyJs_anonymous_123_())
    @Js
    def PyJs_anonymous_129_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['Montgomery'])
        @Js
        def PyJsHoisted_Montgomery_(m, this, arguments, var=var):
            var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['m'])
            var.get(u"this").put('m', var.get('m'))
            var.get(u"this").put('mp', var.get('m').callprop('invDigit'))
            var.get(u"this").put('mpl', (var.get(u"this").get('mp')&Js(32767)))
            var.get(u"this").put('mph', (var.get(u"this").get('mp')>>Js(15.0)))
            var.get(u"this").put('um', ((Js(1.0)<<(var.get('m').get('DB')-Js(15.0)))-Js(1.0)))
            var.get(u"this").put('mt2', (Js(2.0)*var.get('m').get('t')))
        PyJsHoisted_Montgomery_.func_name = 'Montgomery'
        var.put('Montgomery', PyJsHoisted_Montgomery_)
        pass
        @Js
        def PyJs_anonymous_130_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x', 'r'])
            var.put('r', var.get('nbi')())
            var.get('x').callprop('abs').callprop('dlShiftTo', var.get(u"this").get('m').get('t'), var.get('r'))
            var.get('r').callprop('divRemTo', var.get(u"this").get('m'), var.get(u"null"), var.get('r'))
            if ((var.get('x').get('s')<Js(0.0)) and (var.get('r').callprop('compareTo', var.get('BigInteger').get('ZERO'))>Js(0.0))):
                var.get(u"this").get('m').callprop('subTo', var.get('r'), var.get('r'))
            return var.get('r')
        PyJs_anonymous_130_._set_name('anonymous')
        var.get('Montgomery').get('prototype').put('convert', PyJs_anonymous_130_)
        @Js
        def PyJs_anonymous_131_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x', 'r'])
            var.put('r', var.get('nbi')())
            var.get('x').callprop('copyTo', var.get('r'))
            var.get(u"this").callprop('reduce', var.get('r'))
            return var.get('r')
        PyJs_anonymous_131_._set_name('anonymous')
        var.get('Montgomery').get('prototype').put('revert', PyJs_anonymous_131_)
        @Js
        def PyJs_anonymous_132_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'j', 'x', 'u0'])
            while (var.get('x').get('t')<=var.get(u"this").get('mt2')):
                var.get('x').put((var.get('x').put('t',Js(var.get('x').get('t').to_number())+Js(1))-Js(1)), Js(0.0))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get(u"this").get('m').get('t')):
                try:
                    var.put('j', (var.get('x').get(var.get('i'))&Js(32767)))
                    var.put('u0', (((var.get('j')*var.get(u"this").get('mpl'))+((((var.get('j')*var.get(u"this").get('mph'))+((var.get('x').get(var.get('i'))>>Js(15.0))*var.get(u"this").get('mpl')))&var.get(u"this").get('um'))<<Js(15.0)))&var.get('x').get('DM')))
                    var.put('j', (var.get('i')+var.get(u"this").get('m').get('t')))
                    var.get('x').put(var.get('j'), var.get(u"this").get('m').callprop('am', Js(0.0), var.get('u0'), var.get('x'), var.get('i'), Js(0.0), var.get(u"this").get('m').get('t')), '+')
                    while (var.get('x').get(var.get('j'))>=var.get('x').get('DV')):
                        var.get('x').put(var.get('j'), var.get('x').get('DV'), '-')
                        (var.get('x').put(var.put('j',Js(var.get('j').to_number())+Js(1)),Js(var.get('x').get(var.put('j',Js(var.get('j').to_number())+Js(1))).to_number())+Js(1))-Js(1))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            var.get('x').callprop('clamp')
            var.get('x').callprop('drShiftTo', var.get(u"this").get('m').get('t'), var.get('x'))
            if (var.get('x').callprop('compareTo', var.get(u"this").get('m'))>=Js(0.0)):
                var.get('x').callprop('subTo', var.get(u"this").get('m'), var.get('x'))
        PyJs_anonymous_132_._set_name('anonymous')
        var.get('Montgomery').get('prototype').put('reduce', PyJs_anonymous_132_)
        @Js
        def PyJs_anonymous_133_(x, y, r, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x', 'r'])
            var.get('x').callprop('multiplyTo', var.get('y'), var.get('r'))
            var.get(u"this").callprop('reduce', var.get('r'))
        PyJs_anonymous_133_._set_name('anonymous')
        var.get('Montgomery').get('prototype').put('mulTo', PyJs_anonymous_133_)
        @Js
        def PyJs_anonymous_134_(x, r, this, arguments, var=var):
            var = Scope({'x':x, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['x', 'r'])
            var.get('x').callprop('squareTo', var.get('r'))
            var.get(u"this").callprop('reduce', var.get('r'))
        PyJs_anonymous_134_._set_name('anonymous')
        var.get('Montgomery').get('prototype').put('sqrTo', PyJs_anonymous_134_)
        return var.get('Montgomery')
    PyJs_anonymous_129_._set_name('anonymous')
    var.put('Montgomery', PyJs_anonymous_129_())
    @Js
    def PyJs_anonymous_135_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['Barrett'])
        @Js
        def PyJsHoisted_Barrett_(m, this, arguments, var=var):
            var = Scope({'m':m, 'this':this, 'arguments':arguments}, var)
            var.registers(['m'])
            var.get(u"this").put('m', var.get('m'))
            var.get(u"this").put('r2', var.get('nbi')())
            var.get(u"this").put('q3', var.get('nbi')())
            var.get('BigInteger').get('ONE').callprop('dlShiftTo', (Js(2.0)*var.get('m').get('t')), var.get(u"this").get('r2'))
            var.get(u"this").put('mu', var.get(u"this").get('r2').callprop('divide', var.get('m')))
        PyJsHoisted_Barrett_.func_name = 'Barrett'
        var.put('Barrett', PyJsHoisted_Barrett_)
        pass
        @Js
        def PyJs_anonymous_136_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x', 'r'])
            if ((var.get('x').get('s')<Js(0.0)) or (var.get('x').get('t')>(Js(2.0)*var.get(u"this").get('m').get('t')))):
                return var.get('x').callprop('mod', var.get(u"this").get('m'))
            else:
                if (var.get('x').callprop('compareTo', var.get(u"this").get('m'))<Js(0.0)):
                    return var.get('x')
                else:
                    var.put('r', var.get('nbi')())
                    var.get('x').callprop('copyTo', var.get('r'))
                    var.get(u"this").callprop('reduce', var.get('r'))
                    return var.get('r')
        PyJs_anonymous_136_._set_name('anonymous')
        var.get('Barrett').get('prototype').put('convert', PyJs_anonymous_136_)
        @Js
        def PyJs_anonymous_137_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x'])
            return var.get('x')
        PyJs_anonymous_137_._set_name('anonymous')
        var.get('Barrett').get('prototype').put('revert', PyJs_anonymous_137_)
        @Js
        def PyJs_anonymous_138_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x'])
            var.get('x').callprop('drShiftTo', (var.get(u"this").get('m').get('t')-Js(1.0)), var.get(u"this").get('r2'))
            if (var.get('x').get('t')>(var.get(u"this").get('m').get('t')+Js(1.0))):
                var.get('x').put('t', (var.get(u"this").get('m').get('t')+Js(1.0)))
                var.get('x').callprop('clamp')
            var.get(u"this").get('mu').callprop('multiplyUpperTo', var.get(u"this").get('r2'), (var.get(u"this").get('m').get('t')+Js(1.0)), var.get(u"this").get('q3'))
            var.get(u"this").get('m').callprop('multiplyLowerTo', var.get(u"this").get('q3'), (var.get(u"this").get('m').get('t')+Js(1.0)), var.get(u"this").get('r2'))
            while (var.get('x').callprop('compareTo', var.get(u"this").get('r2'))<Js(0.0)):
                var.get('x').callprop('dAddOffset', Js(1.0), (var.get(u"this").get('m').get('t')+Js(1.0)))
            var.get('x').callprop('subTo', var.get(u"this").get('r2'), var.get('x'))
            while (var.get('x').callprop('compareTo', var.get(u"this").get('m'))>=Js(0.0)):
                var.get('x').callprop('subTo', var.get(u"this").get('m'), var.get('x'))
        PyJs_anonymous_138_._set_name('anonymous')
        var.get('Barrett').get('prototype').put('reduce', PyJs_anonymous_138_)
        @Js
        def PyJs_anonymous_139_(x, y, r, this, arguments, var=var):
            var = Scope({'x':x, 'y':y, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['y', 'x', 'r'])
            var.get('x').callprop('multiplyTo', var.get('y'), var.get('r'))
            var.get(u"this").callprop('reduce', var.get('r'))
        PyJs_anonymous_139_._set_name('anonymous')
        var.get('Barrett').get('prototype').put('mulTo', PyJs_anonymous_139_)
        @Js
        def PyJs_anonymous_140_(x, r, this, arguments, var=var):
            var = Scope({'x':x, 'r':r, 'this':this, 'arguments':arguments}, var)
            var.registers(['x', 'r'])
            var.get('x').callprop('squareTo', var.get('r'))
            var.get(u"this").callprop('reduce', var.get('r'))
        PyJs_anonymous_140_._set_name('anonymous')
        var.get('Barrett').get('prototype').put('sqrTo', PyJs_anonymous_140_)
        return var.get('Barrett')
    PyJs_anonymous_135_._set_name('anonymous')
    var.put('Barrett', PyJs_anonymous_135_())
    pass
    pass
    pass
    pass
    pass
    if (var.get('j_lm') and (var.get('navigator').get('appName')==Js('Microsoft Internet Explorer'))):
        var.get('BigInteger').get('prototype').put('am', var.get('am2'))
        var.put('dbits', Js(30.0))
    else:
        if (var.get('j_lm') and (var.get('navigator').get('appName')!=Js('Netscape'))):
            var.get('BigInteger').get('prototype').put('am', var.get('am1'))
            var.put('dbits', Js(26.0))
        else:
            var.get('BigInteger').get('prototype').put('am', var.get('am3'))
            var.put('dbits', Js(28.0))
    var.get('BigInteger').get('prototype').put('DB', var.get('dbits'))
    var.get('BigInteger').get('prototype').put('DM', ((Js(1.0)<<var.get('dbits'))-Js(1.0)))
    var.get('BigInteger').get('prototype').put('DV', (Js(1.0)<<var.get('dbits')))
    var.put('BI_FP', Js(52.0))
    var.get('BigInteger').get('prototype').put('FV', var.get('Math').callprop('pow', Js(2.0), var.get('BI_FP')))
    var.get('BigInteger').get('prototype').put('F1', (var.get('BI_FP')-var.get('dbits')))
    var.get('BigInteger').get('prototype').put('F2', ((Js(2.0)*var.get('dbits'))-var.get('BI_FP')))
    var.put('BI_RC', Js([]))
    pass
    pass
    var.put('rr', Js('0').callprop('charCodeAt', Js(0.0)))
    #for JS loop
    var.put('vv', Js(0.0))
    while (var.get('vv')<=Js(9.0)):
        try:
            var.get('BI_RC').put((var.put('rr',Js(var.get('rr').to_number())+Js(1))-Js(1)), var.get('vv'))
        finally:
                var.put('vv',Js(var.get('vv').to_number())+Js(1))
    var.put('rr', Js('a').callprop('charCodeAt', Js(0.0)))
    #for JS loop
    var.put('vv', Js(10.0))
    while (var.get('vv')<Js(36.0)):
        try:
            var.get('BI_RC').put((var.put('rr',Js(var.get('rr').to_number())+Js(1))-Js(1)), var.get('vv'))
        finally:
                var.put('vv',Js(var.get('vv').to_number())+Js(1))
    var.put('rr', Js('A').callprop('charCodeAt', Js(0.0)))
    #for JS loop
    var.put('vv', Js(10.0))
    while (var.get('vv')<Js(36.0)):
        try:
            var.get('BI_RC').put((var.put('rr',Js(var.get('rr').to_number())+Js(1))-Js(1)), var.get('vv'))
        finally:
                var.put('vv',Js(var.get('vv').to_number())+Js(1))
    pass
    pass
    pass
    var.get('BigInteger').put('ZERO', var.get('nbv')(Js(0.0)))
    var.get('BigInteger').put('ONE', var.get('nbv')(Js(1.0)))
    @Js
    def PyJs_anonymous_141_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['Arcfour'])
        @Js
        def PyJsHoisted_Arcfour_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            var.get(u"this").put('i', Js(0.0))
            var.get(u"this").put('j', Js(0.0))
            var.get(u"this").put('S', Js([]))
        PyJsHoisted_Arcfour_.func_name = 'Arcfour'
        var.put('Arcfour', PyJsHoisted_Arcfour_)
        pass
        @Js
        def PyJs_anonymous_142_(key, this, arguments, var=var):
            var = Scope({'key':key, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'j', 'key', 't'])
            pass
            pass
            pass
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(256.0)):
                try:
                    var.get(u"this").get('S').put(var.get('i'), var.get('i'))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            var.put('j', Js(0.0))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<Js(256.0)):
                try:
                    var.put('j', (((var.get('j')+var.get(u"this").get('S').get(var.get('i')))+var.get('key').get((var.get('i')%var.get('key').get('length'))))&Js(255.0)))
                    var.put('t', var.get(u"this").get('S').get(var.get('i')))
                    var.get(u"this").get('S').put(var.get('i'), var.get(u"this").get('S').get(var.get('j')))
                    var.get(u"this").get('S').put(var.get('j'), var.get('t'))
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
            var.get(u"this").put('i', Js(0.0))
            var.get(u"this").put('j', Js(0.0))
        PyJs_anonymous_142_._set_name('anonymous')
        var.get('Arcfour').get('prototype').put('init', PyJs_anonymous_142_)
        @Js
        def PyJs_anonymous_143_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['t'])
            pass
            var.get(u"this").put('i', ((var.get(u"this").get('i')+Js(1.0))&Js(255.0)))
            var.get(u"this").put('j', ((var.get(u"this").get('j')+var.get(u"this").get('S').get(var.get(u"this").get('i')))&Js(255.0)))
            var.put('t', var.get(u"this").get('S').get(var.get(u"this").get('i')))
            var.get(u"this").get('S').put(var.get(u"this").get('i'), var.get(u"this").get('S').get(var.get(u"this").get('j')))
            var.get(u"this").get('S').put(var.get(u"this").get('j'), var.get('t'))
            return var.get(u"this").get('S').get(((var.get('t')+var.get(u"this").get('S').get(var.get(u"this").get('i')))&Js(255.0)))
        PyJs_anonymous_143_._set_name('anonymous')
        var.get('Arcfour').get('prototype').put('next', PyJs_anonymous_143_)
        return var.get('Arcfour')
    PyJs_anonymous_141_._set_name('anonymous')
    var.put('Arcfour', PyJs_anonymous_141_())
    pass
    var.put('rng_psize', Js(256.0))
    pass
    var.put('rng_pool', var.get(u"null"))
    pass
    if (var.get('rng_pool')==var.get(u"null")):
        var.put('rng_pool', Js([]))
        var.put('rng_pptr', Js(0.0))
        var.put('t', PyJsComma(Js(0.0), Js(None)))
        if (var.get('window').get('crypto') and var.get('window').get('crypto').get('getRandomValues')):
            var.put('z', var.get('Uint32Array').create(Js(256.0)))
            var.get('window').get('crypto').callprop('getRandomValues', var.get('z'))
            #for JS loop
            var.put('t', Js(0.0))
            while (var.get('t')<var.get('z').get('length')):
                try:
                    var.get('rng_pool').put((var.put('rng_pptr',Js(var.get('rng_pptr').to_number())+Js(1))-Js(1)), (var.get('z').get(var.get('t'))&Js(255.0)))
                finally:
                        var.put('t',Js(var.get('t').to_number())+Js(1))
        @Js
        def PyJs_anonymous_144_(ev, this, arguments, var=var):
            var = Scope({'ev':ev, 'this':this, 'arguments':arguments}, var)
            var.registers(['mouseCoordinates', 'ev'])
            var.get(u"this").put('count', (var.get(u"this").get('count') or Js(0.0)))
            if ((var.get(u"this").get('count')>=Js(256.0)) or (var.get('rng_pptr')>=var.get('rng_psize'))):
                if var.get('window').get('removeEventListener'):
                    var.get('window').callprop('removeEventListener', Js('mousemove'), var.get('onMouseMoveListener_1'), Js(False))
                else:
                    if var.get('window').get('detachEvent'):
                        var.get('window').callprop('detachEvent', Js('onmousemove'), var.get('onMouseMoveListener_1'))
                return var.get('undefined')
            try:
                var.put('mouseCoordinates', (var.get('ev').get('x')+var.get('ev').get('y')))
                var.get('rng_pool').put((var.put('rng_pptr',Js(var.get('rng_pptr').to_number())+Js(1))-Js(1)), (var.get('mouseCoordinates')&Js(255.0)))
                var.get(u"this").put('count', Js(1.0), '+')
            except PyJsException as PyJsTempException:
                PyJsHolder_65_82933401 = var.own.get('e')
                var.force_own_put('e', PyExceptionToJs(PyJsTempException))
                try:
                    pass
                finally:
                    if PyJsHolder_65_82933401 is not None:
                        var.own['e'] = PyJsHolder_65_82933401
                    else:
                        del var.own['e']
                    del PyJsHolder_65_82933401
        PyJs_anonymous_144_._set_name('anonymous')
        var.put('onMouseMoveListener_1', PyJs_anonymous_144_)
        if var.get('window').get('addEventListener'):
            var.get('window').callprop('addEventListener', Js('mousemove'), var.get('onMouseMoveListener_1'), Js(False))
        else:
            if var.get('window').get('attachEvent'):
                var.get('window').callprop('attachEvent', Js('onmousemove'), var.get('onMouseMoveListener_1'))
    pass
    @Js
    def PyJs_anonymous_145_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['SecureRandom'])
        @Js
        def PyJsHoisted_SecureRandom_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            pass
        PyJsHoisted_SecureRandom_.func_name = 'SecureRandom'
        var.put('SecureRandom', PyJsHoisted_SecureRandom_)
        pass
        @Js
        def PyJs_anonymous_146_(ba, this, arguments, var=var):
            var = Scope({'ba':ba, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'ba'])
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('ba').get('length')):
                try:
                    var.get('ba').put(var.get('i'), var.get('rng_get_byte')())
                finally:
                        var.put('i',Js(var.get('i').to_number())+Js(1))
        PyJs_anonymous_146_._set_name('anonymous')
        var.get('SecureRandom').get('prototype').put('nextBytes', PyJs_anonymous_146_)
        return var.get('SecureRandom')
    PyJs_anonymous_145_._set_name('anonymous')
    var.put('SecureRandom', PyJs_anonymous_145_())
    pass
    pass
    @Js
    def PyJs_anonymous_147_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['RSAKey'])
        @Js
        def PyJsHoisted_RSAKey_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            var.get(u"this").put('n', var.get(u"null"))
            var.get(u"this").put('e', Js(0.0))
            var.get(u"this").put('d', var.get(u"null"))
            var.get(u"this").put('p', var.get(u"null"))
            var.get(u"this").put('q', var.get(u"null"))
            var.get(u"this").put('dmp1', var.get(u"null"))
            var.get(u"this").put('dmq1', var.get(u"null"))
            var.get(u"this").put('coeff', var.get(u"null"))
        PyJsHoisted_RSAKey_.func_name = 'RSAKey'
        var.put('RSAKey', PyJsHoisted_RSAKey_)
        pass
        @Js
        def PyJs_anonymous_148_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['x'])
            return var.get('x').callprop('modPowInt', var.get(u"this").get('e'), var.get(u"this").get('n'))
        PyJs_anonymous_148_._set_name('anonymous')
        var.get('RSAKey').get('prototype').put('doPublic', PyJs_anonymous_148_)
        @Js
        def PyJs_anonymous_149_(x, this, arguments, var=var):
            var = Scope({'x':x, 'this':this, 'arguments':arguments}, var)
            var.registers(['xp', 'x', 'xq'])
            if ((var.get(u"this").get('p')==var.get(u"null")) or (var.get(u"this").get('q')==var.get(u"null"))):
                return var.get('x').callprop('modPow', var.get(u"this").get('d'), var.get(u"this").get('n'))
            var.put('xp', var.get('x').callprop('mod', var.get(u"this").get('p')).callprop('modPow', var.get(u"this").get('dmp1'), var.get(u"this").get('p')))
            var.put('xq', var.get('x').callprop('mod', var.get(u"this").get('q')).callprop('modPow', var.get(u"this").get('dmq1'), var.get(u"this").get('q')))
            while (var.get('xp').callprop('compareTo', var.get('xq'))<Js(0.0)):
                var.put('xp', var.get('xp').callprop('add', var.get(u"this").get('p')))
            return var.get('xp').callprop('subtract', var.get('xq')).callprop('multiply', var.get(u"this").get('coeff')).callprop('mod', var.get(u"this").get('p')).callprop('multiply', var.get(u"this").get('q')).callprop('add', var.get('xq'))
        PyJs_anonymous_149_._set_name('anonymous')
        var.get('RSAKey').get('prototype').put('doPrivate', PyJs_anonymous_149_)
        @Js
        def PyJs_anonymous_150_(N, E, this, arguments, var=var):
            var = Scope({'N':N, 'E':E, 'this':this, 'arguments':arguments}, var)
            var.registers(['E', 'N'])
            if ((((var.get('N')!=var.get(u"null")) and (var.get('E')!=var.get(u"null"))) and (var.get('N').get('length')>Js(0.0))) and (var.get('E').get('length')>Js(0.0))):
                var.get(u"this").put('n', var.get('parseBigInt')(var.get('N'), Js(16.0)))
                var.get(u"this").put('e', var.get('parseInt')(var.get('E'), Js(16.0)))
            else:
                var.get('console').callprop('error', Js('Invalid RSA public key'))
        PyJs_anonymous_150_._set_name('anonymous')
        var.get('RSAKey').get('prototype').put('setPublic', PyJs_anonymous_150_)
        @Js
        def PyJs_anonymous_151_(text, this, arguments, var=var):
            var = Scope({'text':text, 'this':this, 'arguments':arguments}, var)
            var.registers(['text', 'h', 'c', 'm'])
            var.put('m', var.get('pkcs1pad2')(var.get('text'), ((var.get(u"this").get('n').callprop('bitLength')+Js(7.0))>>Js(3.0))))
            if (var.get('m')==var.get(u"null")):
                return var.get(u"null")
            var.put('c', var.get(u"this").callprop('doPublic', var.get('m')))
            if (var.get('c')==var.get(u"null")):
                return var.get(u"null")
            var.put('h', var.get('c').callprop('toString', Js(16.0)))
            if ((var.get('h').get('length')&Js(1.0))==Js(0.0)):
                return var.get('h')
            else:
                return (Js('0')+var.get('h'))
        PyJs_anonymous_151_._set_name('anonymous')
        var.get('RSAKey').get('prototype').put('encrypt', PyJs_anonymous_151_)
        @Js
        def PyJs_anonymous_152_(text, this, arguments, var=var):
            var = Scope({'text':text, 'this':this, 'arguments':arguments}, var)
            var.registers(['text', '_this', 'ct_1', 'maxLength', 't', 'y', 'lt'])
            var.put('_this', var.get(u"this"))
            var.put('maxLength', (((var.get(u"this").get('n').callprop('bitLength')+Js(7.0))>>Js(3.0))-Js(11.0)))
            try:
                var.put('ct_1', Js(''))
                if (var.get('text').get('length')>var.get('maxLength')):
                    var.put('lt', var.get('text').callprop('match', JsRegExp('/.{1,117}/g')))
                    @Js
                    def PyJs_anonymous_153_(entry, this, arguments, var=var):
                        var = Scope({'entry':entry, 'this':this, 'arguments':arguments}, var)
                        var.registers(['t1', 'entry'])
                        var.put('t1', var.get('_this').callprop('encrypt', var.get('entry')))
                        var.put('ct_1', var.get('t1'), '+')
                    PyJs_anonymous_153_._set_name('anonymous')
                    var.get('lt').callprop('forEach', PyJs_anonymous_153_)
                    return var.get('hex2b64')(var.get('ct_1'))
                var.put('t', var.get(u"this").callprop('encrypt', var.get('text')))
                var.put('y', var.get('hex2b64')(var.get('t')))
                return var.get('y')
            except PyJsException as PyJsTempException:
                PyJsHolder_6578_54210284 = var.own.get('ex')
                var.force_own_put('ex', PyExceptionToJs(PyJsTempException))
                try:
                    return Js(False)
                finally:
                    if PyJsHolder_6578_54210284 is not None:
                        var.own['ex'] = PyJsHolder_6578_54210284
                    else:
                        del var.own['ex']
                    del PyJsHolder_6578_54210284
        PyJs_anonymous_152_._set_name('anonymous')
        var.get('RSAKey').get('prototype').put('encryptLong', PyJs_anonymous_152_)
        @Js
        def PyJs_anonymous_154_(text, this, arguments, var=var):
            var = Scope({'text':text, 'this':this, 'arguments':arguments}, var)
            var.registers(['text', '_this', 'maxLength', 'ct_2', 'y', 'lt'])
            var.put('_this', var.get(u"this"))
            var.put('maxLength', ((var.get(u"this").get('n').callprop('bitLength')+Js(7.0))>>Js(3.0)))
            var.put('text', var.get('b64tohex')(var.get('text')))
            try:
                if (var.get('text').get('length')>var.get('maxLength')):
                    var.put('ct_2', Js(''))
                    var.put('lt', var.get('text').callprop('match', JsRegExp('/.{1,256}/g')))
                    @Js
                    def PyJs_anonymous_155_(entry, this, arguments, var=var):
                        var = Scope({'entry':entry, 'this':this, 'arguments':arguments}, var)
                        var.registers(['t1', 'entry'])
                        var.put('t1', var.get('_this').callprop('decrypt', var.get('entry')))
                        var.put('ct_2', var.get('t1'), '+')
                    PyJs_anonymous_155_._set_name('anonymous')
                    var.get('lt').callprop('forEach', PyJs_anonymous_155_)
                    return var.get('ct_2')
                var.put('y', var.get(u"this").callprop('decrypt', var.get('text')))
                return var.get('y')
            except PyJsException as PyJsTempException:
                PyJsHolder_6578_38315417 = var.own.get('ex')
                var.force_own_put('ex', PyExceptionToJs(PyJsTempException))
                try:
                    return Js(False)
                finally:
                    if PyJsHolder_6578_38315417 is not None:
                        var.own['ex'] = PyJsHolder_6578_38315417
                    else:
                        del var.own['ex']
                    del PyJsHolder_6578_38315417
        PyJs_anonymous_154_._set_name('anonymous')
        var.get('RSAKey').get('prototype').put('decryptLong', PyJs_anonymous_154_)
        @Js
        def PyJs_anonymous_156_(N, E, D, this, arguments, var=var):
            var = Scope({'N':N, 'E':E, 'D':D, 'this':this, 'arguments':arguments}, var)
            var.registers(['E', 'N', 'D'])
            if ((((var.get('N')!=var.get(u"null")) and (var.get('E')!=var.get(u"null"))) and (var.get('N').get('length')>Js(0.0))) and (var.get('E').get('length')>Js(0.0))):
                var.get(u"this").put('n', var.get('parseBigInt')(var.get('N'), Js(16.0)))
                var.get(u"this").put('e', var.get('parseInt')(var.get('E'), Js(16.0)))
                var.get(u"this").put('d', var.get('parseBigInt')(var.get('D'), Js(16.0)))
            else:
                var.get('console').callprop('error', Js('Invalid RSA private key'))
        PyJs_anonymous_156_._set_name('anonymous')
        var.get('RSAKey').get('prototype').put('setPrivate', PyJs_anonymous_156_)
        @Js
        def PyJs_anonymous_157_(N, E, D, P, Q, DP, DQ, C, this, arguments, var=var):
            var = Scope({'N':N, 'E':E, 'D':D, 'P':P, 'Q':Q, 'DP':DP, 'DQ':DQ, 'C':C, 'this':this, 'arguments':arguments}, var)
            var.registers(['DP', 'Q', 'E', 'C', 'DQ', 'P', 'N', 'D'])
            if ((((var.get('N')!=var.get(u"null")) and (var.get('E')!=var.get(u"null"))) and (var.get('N').get('length')>Js(0.0))) and (var.get('E').get('length')>Js(0.0))):
                var.get(u"this").put('n', var.get('parseBigInt')(var.get('N'), Js(16.0)))
                var.get(u"this").put('e', var.get('parseInt')(var.get('E'), Js(16.0)))
                var.get(u"this").put('d', var.get('parseBigInt')(var.get('D'), Js(16.0)))
                var.get(u"this").put('p', var.get('parseBigInt')(var.get('P'), Js(16.0)))
                var.get(u"this").put('q', var.get('parseBigInt')(var.get('Q'), Js(16.0)))
                var.get(u"this").put('dmp1', var.get('parseBigInt')(var.get('DP'), Js(16.0)))
                var.get(u"this").put('dmq1', var.get('parseBigInt')(var.get('DQ'), Js(16.0)))
                var.get(u"this").put('coeff', var.get('parseBigInt')(var.get('C'), Js(16.0)))
            else:
                var.get('console').callprop('error', Js('Invalid RSA private key'))
        PyJs_anonymous_157_._set_name('anonymous')
        var.get('RSAKey').get('prototype').put('setPrivateEx', PyJs_anonymous_157_)
        @Js
        def PyJs_anonymous_158_(B, E, this, arguments, var=var):
            var = Scope({'B':B, 'E':E, 'this':this, 'arguments':arguments}, var)
            var.registers(['q1', 'p1', 'rng', 'phi', 'E', 'ee', 'qs', 't', 'B'])
            var.put('rng', var.get('SecureRandom').create())
            var.put('qs', (var.get('B')>>Js(1.0)))
            var.get(u"this").put('e', var.get('parseInt')(var.get('E'), Js(16.0)))
            var.put('ee', var.get('BigInteger').create(var.get('E'), Js(16.0)))
            #for JS loop
            
            while 1:
                #for JS loop
                
                while 1:
                    var.get(u"this").put('p', var.get('BigInteger').create((var.get('B')-var.get('qs')), Js(1.0), var.get('rng')))
                    if ((var.get(u"this").get('p').callprop('subtract', var.get('BigInteger').get('ONE')).callprop('gcd', var.get('ee')).callprop('compareTo', var.get('BigInteger').get('ONE'))==Js(0.0)) and var.get(u"this").get('p').callprop('isProbablePrime', Js(10.0))):
                        break
                
                #for JS loop
                
                while 1:
                    var.get(u"this").put('q', var.get('BigInteger').create(var.get('qs'), Js(1.0), var.get('rng')))
                    if ((var.get(u"this").get('q').callprop('subtract', var.get('BigInteger').get('ONE')).callprop('gcd', var.get('ee')).callprop('compareTo', var.get('BigInteger').get('ONE'))==Js(0.0)) and var.get(u"this").get('q').callprop('isProbablePrime', Js(10.0))):
                        break
                
                if (var.get(u"this").get('p').callprop('compareTo', var.get(u"this").get('q'))<=Js(0.0)):
                    var.put('t', var.get(u"this").get('p'))
                    var.get(u"this").put('p', var.get(u"this").get('q'))
                    var.get(u"this").put('q', var.get('t'))
                var.put('p1', var.get(u"this").get('p').callprop('subtract', var.get('BigInteger').get('ONE')))
                var.put('q1', var.get(u"this").get('q').callprop('subtract', var.get('BigInteger').get('ONE')))
                var.put('phi', var.get('p1').callprop('multiply', var.get('q1')))
                if (var.get('phi').callprop('gcd', var.get('ee')).callprop('compareTo', var.get('BigInteger').get('ONE'))==Js(0.0)):
                    var.get(u"this").put('n', var.get(u"this").get('p').callprop('multiply', var.get(u"this").get('q')))
                    var.get(u"this").put('d', var.get('ee').callprop('modInverse', var.get('phi')))
                    var.get(u"this").put('dmp1', var.get(u"this").get('d').callprop('mod', var.get('p1')))
                    var.get(u"this").put('dmq1', var.get(u"this").get('d').callprop('mod', var.get('q1')))
                    var.get(u"this").put('coeff', var.get(u"this").get('q').callprop('modInverse', var.get(u"this").get('p')))
                    break
            
        PyJs_anonymous_158_._set_name('anonymous')
        var.get('RSAKey').get('prototype').put('generate', PyJs_anonymous_158_)
        @Js
        def PyJs_anonymous_159_(ctext, this, arguments, var=var):
            var = Scope({'ctext':ctext, 'this':this, 'arguments':arguments}, var)
            var.registers(['ctext', 'c', 'm'])
            var.put('c', var.get('parseBigInt')(var.get('ctext'), Js(16.0)))
            var.put('m', var.get(u"this").callprop('doPrivate', var.get('c')))
            if (var.get('m')==var.get(u"null")):
                return var.get(u"null")
            return var.get('pkcs1unpad2')(var.get('m'), ((var.get(u"this").get('n').callprop('bitLength')+Js(7.0))>>Js(3.0)))
        PyJs_anonymous_159_._set_name('anonymous')
        var.get('RSAKey').get('prototype').put('decrypt', PyJs_anonymous_159_)
        @Js
        def PyJs_anonymous_160_(B, E, callback, this, arguments, var=var):
            var = Scope({'B':B, 'E':E, 'callback':callback, 'this':this, 'arguments':arguments}, var)
            var.registers(['rsa', 'rng', 'E', 'callback', 'ee', 'qs', 'B', 'loop1'])
            var.put('rng', var.get('SecureRandom').create())
            var.put('qs', (var.get('B')>>Js(1.0)))
            var.get(u"this").put('e', var.get('parseInt')(var.get('E'), Js(16.0)))
            var.put('ee', var.get('BigInteger').create(var.get('E'), Js(16.0)))
            var.put('rsa', var.get(u"this"))
            @Js
            def PyJs_anonymous_161_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments}, var)
                var.registers(['loop2', 'loop4', 'loop3'])
                @Js
                def PyJs_anonymous_162_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers(['p1', 'q1', 't', 'phi'])
                    if (var.get('rsa').get('p').callprop('compareTo', var.get('rsa').get('q'))<=Js(0.0)):
                        var.put('t', var.get('rsa').get('p'))
                        var.get('rsa').put('p', var.get('rsa').get('q'))
                        var.get('rsa').put('q', var.get('t'))
                    var.put('p1', var.get('rsa').get('p').callprop('subtract', var.get('BigInteger').get('ONE')))
                    var.put('q1', var.get('rsa').get('q').callprop('subtract', var.get('BigInteger').get('ONE')))
                    var.put('phi', var.get('p1').callprop('multiply', var.get('q1')))
                    if (var.get('phi').callprop('gcd', var.get('ee')).callprop('compareTo', var.get('BigInteger').get('ONE'))==Js(0.0)):
                        var.get('rsa').put('n', var.get('rsa').get('p').callprop('multiply', var.get('rsa').get('q')))
                        var.get('rsa').put('d', var.get('ee').callprop('modInverse', var.get('phi')))
                        var.get('rsa').put('dmp1', var.get('rsa').get('d').callprop('mod', var.get('p1')))
                        var.get('rsa').put('dmq1', var.get('rsa').get('d').callprop('mod', var.get('q1')))
                        var.get('rsa').put('coeff', var.get('rsa').get('q').callprop('modInverse', var.get('rsa').get('p')))
                        @Js
                        def PyJs_anonymous_163_(this, arguments, var=var):
                            var = Scope({'this':this, 'arguments':arguments}, var)
                            var.registers([])
                            var.get('callback')()
                        PyJs_anonymous_163_._set_name('anonymous')
                        var.get('setTimeout')(PyJs_anonymous_163_, Js(0.0))
                    else:
                        var.get('setTimeout')(var.get('loop1'), Js(0.0))
                PyJs_anonymous_162_._set_name('anonymous')
                var.put('loop4', PyJs_anonymous_162_)
                @Js
                def PyJs_anonymous_164_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers([])
                    var.get('rsa').put('q', var.get('nbi')())
                    @Js
                    def PyJs_anonymous_165_(this, arguments, var=var):
                        var = Scope({'this':this, 'arguments':arguments}, var)
                        var.registers([])
                        @Js
                        def PyJs_anonymous_166_(r, this, arguments, var=var):
                            var = Scope({'r':r, 'this':this, 'arguments':arguments}, var)
                            var.registers(['r'])
                            if ((var.get('r').callprop('compareTo', var.get('BigInteger').get('ONE'))==Js(0.0)) and var.get('rsa').get('q').callprop('isProbablePrime', Js(10.0))):
                                var.get('setTimeout')(var.get('loop4'), Js(0.0))
                            else:
                                var.get('setTimeout')(var.get('loop3'), Js(0.0))
                        PyJs_anonymous_166_._set_name('anonymous')
                        var.get('rsa').get('q').callprop('subtract', var.get('BigInteger').get('ONE')).callprop('gcda', var.get('ee'), PyJs_anonymous_166_)
                    PyJs_anonymous_165_._set_name('anonymous')
                    var.get('rsa').get('q').callprop('fromNumberAsync', var.get('qs'), Js(1.0), var.get('rng'), PyJs_anonymous_165_)
                PyJs_anonymous_164_._set_name('anonymous')
                var.put('loop3', PyJs_anonymous_164_)
                @Js
                def PyJs_anonymous_167_(this, arguments, var=var):
                    var = Scope({'this':this, 'arguments':arguments}, var)
                    var.registers([])
                    var.get('rsa').put('p', var.get('nbi')())
                    @Js
                    def PyJs_anonymous_168_(this, arguments, var=var):
                        var = Scope({'this':this, 'arguments':arguments}, var)
                        var.registers([])
                        @Js
                        def PyJs_anonymous_169_(r, this, arguments, var=var):
                            var = Scope({'r':r, 'this':this, 'arguments':arguments}, var)
                            var.registers(['r'])
                            if ((var.get('r').callprop('compareTo', var.get('BigInteger').get('ONE'))==Js(0.0)) and var.get('rsa').get('p').callprop('isProbablePrime', Js(10.0))):
                                var.get('setTimeout')(var.get('loop3'), Js(0.0))
                            else:
                                var.get('setTimeout')(var.get('loop2'), Js(0.0))
                        PyJs_anonymous_169_._set_name('anonymous')
                        var.get('rsa').get('p').callprop('subtract', var.get('BigInteger').get('ONE')).callprop('gcda', var.get('ee'), PyJs_anonymous_169_)
                    PyJs_anonymous_168_._set_name('anonymous')
                    var.get('rsa').get('p').callprop('fromNumberAsync', (var.get('B')-var.get('qs')), Js(1.0), var.get('rng'), PyJs_anonymous_168_)
                PyJs_anonymous_167_._set_name('anonymous')
                var.put('loop2', PyJs_anonymous_167_)
                var.get('setTimeout')(var.get('loop2'), Js(0.0))
            PyJs_anonymous_161_._set_name('anonymous')
            var.put('loop1', PyJs_anonymous_161_)
            var.get('setTimeout')(var.get('loop1'), Js(0.0))
        PyJs_anonymous_160_._set_name('anonymous')
        var.get('RSAKey').get('prototype').put('generateAsync', PyJs_anonymous_160_)
        @Js
        def PyJs_anonymous_170_(text, digestMethod, digestName, this, arguments, var=var):
            var = Scope({'text':text, 'digestMethod':digestMethod, 'digestName':digestName, 'this':this, 'arguments':arguments}, var)
            var.registers(['text', 'm', 'digestMethod', 'digest', 'c', 'header', 'h', 'digestName'])
            var.put('header', var.get('getDigestHeader')(var.get('digestName')))
            var.put('digest', (var.get('header')+var.get('digestMethod')(var.get('text')).callprop('toString')))
            var.put('m', var.get('pkcs1pad1')(var.get('digest'), (var.get(u"this").get('n').callprop('bitLength')/Js(4.0))))
            if (var.get('m')==var.get(u"null")):
                return var.get(u"null")
            var.put('c', var.get(u"this").callprop('doPrivate', var.get('m')))
            if (var.get('c')==var.get(u"null")):
                return var.get(u"null")
            var.put('h', var.get('c').callprop('toString', Js(16.0)))
            if ((var.get('h').get('length')&Js(1.0))==Js(0.0)):
                return var.get('h')
            else:
                return (Js('0')+var.get('h'))
        PyJs_anonymous_170_._set_name('anonymous')
        var.get('RSAKey').get('prototype').put('sign', PyJs_anonymous_170_)
        @Js
        def PyJs_anonymous_171_(text, signature, digestMethod, this, arguments, var=var):
            var = Scope({'text':text, 'signature':signature, 'digestMethod':digestMethod, 'this':this, 'arguments':arguments}, var)
            var.registers(['text', 'm', 'digestMethod', 'digest', 'c', 'unpadded', 'signature'])
            var.put('c', var.get('parseBigInt')(var.get('signature'), Js(16.0)))
            var.put('m', var.get(u"this").callprop('doPublic', var.get('c')))
            if (var.get('m')==var.get(u"null")):
                return var.get(u"null")
            var.put('unpadded', var.get('m').callprop('toString', Js(16.0)).callprop('replace', JsRegExp('/^1f+00/'), Js('')))
            var.put('digest', var.get('removeDigestHeader')(var.get('unpadded')))
            return (var.get('digest')==var.get('digestMethod')(var.get('text')).callprop('toString'))
        PyJs_anonymous_171_._set_name('anonymous')
        var.get('RSAKey').get('prototype').put('verify', PyJs_anonymous_171_)
        return var.get('RSAKey')
    PyJs_anonymous_147_._set_name('anonymous')
    var.put('RSAKey', PyJs_anonymous_147_())
    pass
    var.put('DIGEST_HEADERS', Js({'md2':Js('3020300c06082a864886f70d020205000410'),'md5':Js('3020300c06082a864886f70d020505000410'),'sha1':Js('3021300906052b0e03021a05000414'),'sha224':Js('302d300d06096086480165030402040500041c'),'sha256':Js('3031300d060960864801650304020105000420'),'sha384':Js('3041300d060960864801650304020205000430'),'sha512':Js('3051300d060960864801650304020305000440'),'ripemd160':Js('3021300906052b2403020105000414')}))
    pass
    pass
    var.put('YAHOO', Js({}))
    @Js
    def PyJs_anonymous_172_(subc, superc, overrides, this, arguments, var=var):
        var = Scope({'subc':subc, 'superc':superc, 'overrides':overrides, 'this':this, 'arguments':arguments}, var)
        var.registers(['overrides', 'superc', '_IEEnumFix', 'ADD', 'i', 'subc', 'F'])
        if (var.get('superc').neg() or var.get('subc').neg()):
            PyJsTempException = JsToPyException(var.get('Error').create((Js('YAHOO.lang.extend failed, please check that ')+Js('all dependencies are included.'))))
            raise PyJsTempException
        @Js
        def PyJs_anonymous_173_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            pass
        PyJs_anonymous_173_._set_name('anonymous')
        var.put('F', PyJs_anonymous_173_)
        var.get('F').put('prototype', var.get('superc').get('prototype'))
        var.get('subc').put('prototype', var.get('F').create())
        var.get('subc').get('prototype').put('constructor', var.get('subc'))
        var.get('subc').put('superclass', var.get('superc').get('prototype'))
        if (var.get('superc').get('prototype').get('constructor')==var.get('Object').get('prototype').get('constructor')):
            var.get('superc').get('prototype').put('constructor', var.get('superc'))
        if var.get('overrides'):
            pass
            for PyJsTemp in var.get('overrides'):
                var.put('i', PyJsTemp)
                var.get('subc').get('prototype').put(var.get('i'), var.get('overrides').get(var.get('i')))
            @Js
            def PyJs_anonymous_174_(this, arguments, var=var):
                var = Scope({'this':this, 'arguments':arguments}, var)
                var.registers([])
                pass
            PyJs_anonymous_174_._set_name('anonymous')
            var.put('_IEEnumFix', PyJs_anonymous_174_)
            var.put('ADD', Js([Js('toString'), Js('valueOf')]))
            try:
                if JsRegExp('/MSIE/').callprop('test', var.get('navigator').get('userAgent')):
                    @Js
                    def PyJs_anonymous_175_(r, s, this, arguments, var=var):
                        var = Scope({'r':r, 's':s, 'this':this, 'arguments':arguments}, var)
                        var.registers(['r', 'f', 'fname', 's'])
                        #for JS loop
                        var.put('i', Js(0.0))
                        while (var.get('i')<var.get('ADD').get('length')):
                            try:
                                var.put('fname', var.get('ADD').get(var.get('i')))
                                var.put('f', var.get('s').get(var.get('fname')))
                                if (PyJsStrictEq(var.get('f',throw=False).typeof(),Js('function')) and (var.get('f')!=var.get('Object').get('prototype').get(var.get('fname')))):
                                    var.get('r').put(var.get('fname'), var.get('f'))
                            finally:
                                    var.put('i', (var.get('i')+Js(1.0)))
                    PyJs_anonymous_175_._set_name('anonymous')
                    var.put('_IEEnumFix', PyJs_anonymous_175_)
            except PyJsException as PyJsTempException:
                PyJsHolder_6578_93428877 = var.own.get('ex')
                var.force_own_put('ex', PyExceptionToJs(PyJsTempException))
                try:
                    pass
                finally:
                    if PyJsHolder_6578_93428877 is not None:
                        var.own['ex'] = PyJsHolder_6578_93428877
                    else:
                        del var.own['ex']
                    del PyJsHolder_6578_93428877
            var.get('_IEEnumFix')(var.get('subc').get('prototype'), var.get('overrides'))
    PyJs_anonymous_172_._set_name('anonymous')
    var.get('YAHOO').put('lang', Js({'extend':PyJs_anonymous_172_}))
    var.put('KJUR', Js({}))
    if ((var.get('KJUR').get('asn1').typeof()==Js('undefined')) or var.get('KJUR').get('asn1').neg()):
        var.get('KJUR').put('asn1', Js({}))
    @Js
    def PyJs_anonymous_176_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        @Js
        def PyJs_anonymous_177_(i, this, arguments, var=var):
            var = Scope({'i':i, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'h'])
            var.put('h', var.get('i').callprop('toString', Js(16.0)))
            if ((var.get('h').get('length')%Js(2.0))==Js(1.0)):
                var.put('h', (Js('0')+var.get('h')))
            return var.get('h')
        PyJs_anonymous_177_._set_name('anonymous')
        var.get(u"this").put('integerToByteHex', PyJs_anonymous_177_)
        @Js
        def PyJs_anonymous_178_(bigIntegerValue, this, arguments, var=var):
            var = Scope({'bigIntegerValue':bigIntegerValue, 'this':this, 'arguments':arguments}, var)
            var.registers(['biMask', 'hPos', 'biNeg', 'hMask', 'i', 'bigIntegerValue', 'h', 'xorLen'])
            var.put('h', var.get('bigIntegerValue').callprop('toString', Js(16.0)))
            if (var.get('h').callprop('substr', Js(0.0), Js(1.0))!=Js('-')):
                if ((var.get('h').get('length')%Js(2.0))==Js(1.0)):
                    var.put('h', (Js('0')+var.get('h')))
                else:
                    if var.get('h').callprop('match', JsRegExp('/^[0-7]/')).neg():
                        var.put('h', (Js('00')+var.get('h')))
            else:
                var.put('hPos', var.get('h').callprop('substr', Js(1.0)))
                var.put('xorLen', var.get('hPos').get('length'))
                if ((var.get('xorLen')%Js(2.0))==Js(1.0)):
                    var.put('xorLen', Js(1.0), '+')
                else:
                    if var.get('h').callprop('match', JsRegExp('/^[0-7]/')).neg():
                        var.put('xorLen', Js(2.0), '+')
                var.put('hMask', Js(''))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('xorLen')):
                    try:
                        var.put('hMask', Js('f'), '+')
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                var.put('biMask', var.get('BigInteger').create(var.get('hMask'), Js(16.0)))
                var.put('biNeg', var.get('biMask').callprop('xor', var.get('bigIntegerValue')).callprop('add', var.get('BigInteger').get('ONE')))
                var.put('h', var.get('biNeg').callprop('toString', Js(16.0)).callprop('replace', JsRegExp('/^-/'), Js('')))
            return var.get('h')
        PyJs_anonymous_178_._set_name('anonymous')
        var.get(u"this").put('bigIntToMinTwosComplementsHex', PyJs_anonymous_178_)
        @Js
        def PyJs_anonymous_179_(dataHex, pemHeader, this, arguments, var=var):
            var = Scope({'dataHex':dataHex, 'pemHeader':pemHeader, 'this':this, 'arguments':arguments}, var)
            var.registers(['dataHex', 'pemHeader'])
            return var.get('hextopem')(var.get('dataHex'), var.get('pemHeader'))
        PyJs_anonymous_179_._set_name('anonymous')
        var.get(u"this").put('getPEMStringFromHex', PyJs_anonymous_179_)
        @Js
        def PyJs_anonymous_180_(param, this, arguments, var=var):
            var = Scope({'param':param, 'this':this, 'arguments':arguments}, var)
            var.registers(['_DERGeneralizedTime', '_DERTaggedObject', 'paramList', '_DERNull', 'newParam', '_DEREnumerated', '_KJUR', 'key', 'a', '_DERSet', '_KJUR_asn1', '_DERTeletexString', '_DERUTCTime', '_DERInteger', '_DERSequence', '_newObject', '_DERBoolean', 'keys', 'obj', 'i', '_DERIA5String', 'param', '_DERBitString', 'tagParam', '_DERObjectIdentifier', 'asn1Obj', '_DERPrintableString', '_DERUTF8String', '_DEROctetString', '_DERNumericString'])
            var.put('_KJUR', var.get('KJUR'))
            var.put('_KJUR_asn1', var.get('_KJUR').get('asn1'))
            var.put('_DERBoolean', var.get('_KJUR_asn1').get('DERBoolean'))
            var.put('_DERInteger', var.get('_KJUR_asn1').get('DERInteger'))
            var.put('_DERBitString', var.get('_KJUR_asn1').get('DERBitString'))
            var.put('_DEROctetString', var.get('_KJUR_asn1').get('DEROctetString'))
            var.put('_DERNull', var.get('_KJUR_asn1').get('DERNull'))
            var.put('_DERObjectIdentifier', var.get('_KJUR_asn1').get('DERObjectIdentifier'))
            var.put('_DEREnumerated', var.get('_KJUR_asn1').get('DEREnumerated'))
            var.put('_DERUTF8String', var.get('_KJUR_asn1').get('DERUTF8String'))
            var.put('_DERNumericString', var.get('_KJUR_asn1').get('DERNumericString'))
            var.put('_DERPrintableString', var.get('_KJUR_asn1').get('DERPrintableString'))
            var.put('_DERTeletexString', var.get('_KJUR_asn1').get('DERTeletexString'))
            var.put('_DERIA5String', var.get('_KJUR_asn1').get('DERIA5String'))
            var.put('_DERUTCTime', var.get('_KJUR_asn1').get('DERUTCTime'))
            var.put('_DERGeneralizedTime', var.get('_KJUR_asn1').get('DERGeneralizedTime'))
            var.put('_DERSequence', var.get('_KJUR_asn1').get('DERSequence'))
            var.put('_DERSet', var.get('_KJUR_asn1').get('DERSet'))
            var.put('_DERTaggedObject', var.get('_KJUR_asn1').get('DERTaggedObject'))
            var.put('_newObject', var.get('_KJUR_asn1').get('ASN1Util').get('newObject'))
            var.put('keys', var.get('Object').callprop('keys', var.get('param')))
            if (var.get('keys').get('length')!=Js(1.0)):
                PyJsTempException = JsToPyException(Js('key of param shall be only one.'))
                raise PyJsTempException
            var.put('key', var.get('keys').get('0'))
            if (Js(':bool:int:bitstr:octstr:null:oid:enum:utf8str:numstr:prnstr:telstr:ia5str:utctime:gentime:seq:set:tag:').callprop('indexOf', ((Js(':')+var.get('key'))+Js(':')))==(-Js(1.0))):
                PyJsTempException = JsToPyException((Js('undefined key: ')+var.get('key')))
                raise PyJsTempException
            if (var.get('key')==Js('bool')):
                return var.get('_DERBoolean').create(var.get('param').get(var.get('key')))
            if (var.get('key')==Js('int')):
                return var.get('_DERInteger').create(var.get('param').get(var.get('key')))
            if (var.get('key')==Js('bitstr')):
                return var.get('_DERBitString').create(var.get('param').get(var.get('key')))
            if (var.get('key')==Js('octstr')):
                return var.get('_DEROctetString').create(var.get('param').get(var.get('key')))
            if (var.get('key')==Js('null')):
                return var.get('_DERNull').create(var.get('param').get(var.get('key')))
            if (var.get('key')==Js('oid')):
                return var.get('_DERObjectIdentifier').create(var.get('param').get(var.get('key')))
            if (var.get('key')==Js('enum')):
                return var.get('_DEREnumerated').create(var.get('param').get(var.get('key')))
            if (var.get('key')==Js('utf8str')):
                return var.get('_DERUTF8String').create(var.get('param').get(var.get('key')))
            if (var.get('key')==Js('numstr')):
                return var.get('_DERNumericString').create(var.get('param').get(var.get('key')))
            if (var.get('key')==Js('prnstr')):
                return var.get('_DERPrintableString').create(var.get('param').get(var.get('key')))
            if (var.get('key')==Js('telstr')):
                return var.get('_DERTeletexString').create(var.get('param').get(var.get('key')))
            if (var.get('key')==Js('ia5str')):
                return var.get('_DERIA5String').create(var.get('param').get(var.get('key')))
            if (var.get('key')==Js('utctime')):
                return var.get('_DERUTCTime').create(var.get('param').get(var.get('key')))
            if (var.get('key')==Js('gentime')):
                return var.get('_DERGeneralizedTime').create(var.get('param').get(var.get('key')))
            if (var.get('key')==Js('seq')):
                var.put('paramList', var.get('param').get(var.get('key')))
                var.put('a', Js([]))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('paramList').get('length')):
                    try:
                        var.put('asn1Obj', var.get('_newObject')(var.get('paramList').get(var.get('i'))))
                        var.get('a').callprop('push', var.get('asn1Obj'))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                return var.get('_DERSequence').create(Js({'array':var.get('a')}))
            if (var.get('key')==Js('set')):
                var.put('paramList', var.get('param').get(var.get('key')))
                var.put('a', Js([]))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<var.get('paramList').get('length')):
                    try:
                        var.put('asn1Obj', var.get('_newObject')(var.get('paramList').get(var.get('i'))))
                        var.get('a').callprop('push', var.get('asn1Obj'))
                    finally:
                            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                return var.get('_DERSet').create(Js({'array':var.get('a')}))
            if (var.get('key')==Js('tag')):
                var.put('tagParam', var.get('param').get(var.get('key')))
                if (PyJsStrictEq(var.get('Object').get('prototype').get('toString').callprop('call', var.get('tagParam')),Js('[object Array]')) and (var.get('tagParam').get('length')==Js(3.0))):
                    var.put('obj', var.get('_newObject')(var.get('tagParam').get('2')))
                    return var.get('_DERTaggedObject').create(Js({'tag':var.get('tagParam').get('0'),'explicit':var.get('tagParam').get('1'),'obj':var.get('obj')}))
                else:
                    var.put('newParam', Js({}))
                    if PyJsStrictNeq(var.get('tagParam').get('explicit'),var.get('undefined')):
                        var.get('newParam').put('explicit', var.get('tagParam').get('explicit'))
                    if PyJsStrictNeq(var.get('tagParam').get('tag'),var.get('undefined')):
                        var.get('newParam').put('tag', var.get('tagParam').get('tag'))
                    if PyJsStrictEq(var.get('tagParam').get('obj'),var.get('undefined')):
                        PyJsTempException = JsToPyException(Js("obj shall be specified for 'tag'."))
                        raise PyJsTempException
                    var.get('newParam').put('obj', var.get('_newObject')(var.get('tagParam').get('obj')))
                    return var.get('_DERTaggedObject').create(var.get('newParam'))
        PyJs_anonymous_180_._set_name('anonymous')
        var.get(u"this").put('newObject', PyJs_anonymous_180_)
        @Js
        def PyJs_anonymous_181_(param, this, arguments, var=var):
            var = Scope({'param':param, 'this':this, 'arguments':arguments}, var)
            var.registers(['param', 'asn1Obj'])
            var.put('asn1Obj', var.get(u"this").callprop('newObject', var.get('param')))
            return var.get('asn1Obj').callprop('getEncodedHex')
        PyJs_anonymous_181_._set_name('anonymous')
        var.get(u"this").put('jsonToASN1HEX', PyJs_anonymous_181_)
    PyJs_anonymous_176_._set_name('anonymous')
    var.get('KJUR').get('asn1').put('ASN1Util', PyJs_anonymous_176_.create())
    @Js
    def PyJs_anonymous_182_(hex, this, arguments, var=var):
        var = Scope({'hex':hex, 'this':this, 'arguments':arguments}, var)
        var.registers(['i01', 'hex', 'i1', 'bin', 'bi', 'binbuf', 'i', 'i0', 'value', 's'])
        var.put('s', Js(''))
        var.put('i01', var.get('parseInt')(var.get('hex').callprop('substr', Js(0.0), Js(2.0)), Js(16.0)))
        var.put('i0', var.get('Math').callprop('floor', (var.get('i01')/Js(40.0))))
        var.put('i1', (var.get('i01')%Js(40.0)))
        var.put('s', ((var.get('i0')+Js('.'))+var.get('i1')))
        var.put('binbuf', Js(''))
        #for JS loop
        var.put('i', Js(2.0))
        while (var.get('i')<var.get('hex').get('length')):
            try:
                var.put('value', var.get('parseInt')(var.get('hex').callprop('substr', var.get('i'), Js(2.0)), Js(16.0)))
                var.put('bin', (Js('00000000')+var.get('value').callprop('toString', Js(2.0))).callprop('slice', (-Js(8.0))))
                var.put('binbuf', (var.get('binbuf')+var.get('bin').callprop('substr', Js(1.0), Js(7.0))))
                if (var.get('bin').callprop('substr', Js(0.0), Js(1.0))==Js('0')):
                    var.put('bi', var.get('BigInteger').create(var.get('binbuf'), Js(2.0)))
                    var.put('s', ((var.get('s')+Js('.'))+var.get('bi').callprop('toString', Js(10.0))))
                    var.put('binbuf', Js(''))
            finally:
                    var.put('i', Js(2.0), '+')
        return var.get('s')
    PyJs_anonymous_182_._set_name('anonymous')
    var.get('KJUR').get('asn1').get('ASN1Util').put('oidHexToInt', PyJs_anonymous_182_)
    @Js
    def PyJs_anonymous_183_(oidString, this, arguments, var=var):
        var = Scope({'oidString':oidString, 'this':this, 'arguments':arguments}, var)
        var.registers(['roidtox', 'a', 'oidString', 'i', 'itox', 'i0', 'h'])
        @Js
        def PyJs_anonymous_184_(i, this, arguments, var=var):
            var = Scope({'i':i, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'h'])
            var.put('h', var.get('i').callprop('toString', Js(16.0)))
            if (var.get('h').get('length')==Js(1.0)):
                var.put('h', (Js('0')+var.get('h')))
            return var.get('h')
        PyJs_anonymous_184_._set_name('anonymous')
        var.put('itox', PyJs_anonymous_184_)
        @Js
        def PyJs_anonymous_185_(roid, this, arguments, var=var):
            var = Scope({'roid':roid, 'this':this, 'arguments':arguments}, var)
            var.registers(['b', 'roid', 'bPad', 'padLen', 'bi', 'b8', 'i', 'h'])
            var.put('h', Js(''))
            var.put('bi', var.get('BigInteger').create(var.get('roid'), Js(10.0)))
            var.put('b', var.get('bi').callprop('toString', Js(2.0)))
            var.put('padLen', (Js(7.0)-(var.get('b').get('length')%Js(7.0))))
            if (var.get('padLen')==Js(7.0)):
                var.put('padLen', Js(0.0))
            var.put('bPad', Js(''))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('padLen')):
                try:
                    var.put('bPad', Js('0'), '+')
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('b', (var.get('bPad')+var.get('b')))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<(var.get('b').get('length')-Js(1.0))):
                try:
                    var.put('b8', var.get('b').callprop('substr', var.get('i'), Js(7.0)))
                    if (var.get('i')!=(var.get('b').get('length')-Js(7.0))):
                        var.put('b8', (Js('1')+var.get('b8')))
                    var.put('h', var.get('itox')(var.get('parseInt')(var.get('b8'), Js(2.0))), '+')
                finally:
                        var.put('i', Js(7.0), '+')
            return var.get('h')
        PyJs_anonymous_185_._set_name('anonymous')
        var.put('roidtox', PyJs_anonymous_185_)
        if var.get('oidString').callprop('match', JsRegExp('/^[0-9.]+$/')).neg():
            PyJsTempException = JsToPyException((Js('malformed oid string: ')+var.get('oidString')))
            raise PyJsTempException
        var.put('h', Js(''))
        var.put('a', var.get('oidString').callprop('split', Js('.')))
        var.put('i0', ((var.get('parseInt')(var.get('a').get('0'))*Js(40.0))+var.get('parseInt')(var.get('a').get('1'))))
        var.put('h', var.get('itox')(var.get('i0')), '+')
        var.get('a').callprop('splice', Js(0.0), Js(2.0))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('a').get('length')):
            try:
                var.put('h', var.get('roidtox')(var.get('a').get(var.get('i'))), '+')
            finally:
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        return var.get('h')
    PyJs_anonymous_183_._set_name('anonymous')
    var.get('KJUR').get('asn1').get('ASN1Util').put('oidIntToHex', PyJs_anonymous_183_)
    @Js
    def PyJs_anonymous_186_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['hV'])
        var.put('hV', Js(''))
        @Js
        def PyJs_anonymous_187_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['hNlen', 'hN', 'n', 'head'])
            if ((var.get(u"this").get('hV').typeof()==Js('undefined')) or (var.get(u"this").get('hV')==var.get(u"null"))):
                PyJsTempException = JsToPyException(Js('this.hV is null or undefined.'))
                raise PyJsTempException
            if ((var.get(u"this").get('hV').get('length')%Js(2.0))==Js(1.0)):
                PyJsTempException = JsToPyException((((Js('value hex must be even length: n=')+var.get('hV').get('length'))+Js(',v='))+var.get(u"this").get('hV')))
                raise PyJsTempException
            var.put('n', (var.get(u"this").get('hV').get('length')/Js(2.0)))
            var.put('hN', var.get('n').callprop('toString', Js(16.0)))
            if ((var.get('hN').get('length')%Js(2.0))==Js(1.0)):
                var.put('hN', (Js('0')+var.get('hN')))
            if (var.get('n')<Js(128.0)):
                return var.get('hN')
            else:
                var.put('hNlen', (var.get('hN').get('length')/Js(2.0)))
                if (var.get('hNlen')>Js(15.0)):
                    PyJsTempException = JsToPyException((Js('ASN.1 length too long to represent by 8x: n = ')+var.get('n').callprop('toString', Js(16.0))))
                    raise PyJsTempException
                var.put('head', (Js(128.0)+var.get('hNlen')))
                return (var.get('head').callprop('toString', Js(16.0))+var.get('hN'))
        PyJs_anonymous_187_._set_name('anonymous')
        var.get(u"this").put('getLengthHexFromValue', PyJs_anonymous_187_)
        @Js
        def PyJs_anonymous_188_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            if ((var.get(u"this").get('hTLV')==var.get(u"null")) or var.get(u"this").get('isModified')):
                var.get(u"this").put('hV', var.get(u"this").callprop('getFreshValueHex'))
                var.get(u"this").put('hL', var.get(u"this").callprop('getLengthHexFromValue'))
                var.get(u"this").put('hTLV', ((var.get(u"this").get('hT')+var.get(u"this").get('hL'))+var.get(u"this").get('hV')))
                var.get(u"this").put('isModified', Js(False))
            return var.get(u"this").get('hTLV')
        PyJs_anonymous_188_._set_name('anonymous')
        var.get(u"this").put('getEncodedHex', PyJs_anonymous_188_)
        @Js
        def PyJs_anonymous_189_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            var.get(u"this").callprop('getEncodedHex')
            return var.get(u"this").get('hV')
        PyJs_anonymous_189_._set_name('anonymous')
        var.get(u"this").put('getValueHex', PyJs_anonymous_189_)
        @Js
        def PyJs_anonymous_190_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return Js('')
        PyJs_anonymous_190_._set_name('anonymous')
        var.get(u"this").put('getFreshValueHex', PyJs_anonymous_190_)
    PyJs_anonymous_186_._set_name('anonymous')
    var.get('KJUR').get('asn1').put('ASN1Object', PyJs_anonymous_186_)
    @Js
    def PyJs_anonymous_191_(params, this, arguments, var=var):
        var = Scope({'params':params, 'this':this, 'arguments':arguments}, var)
        var.registers(['params'])
        var.get('KJUR').get('asn1').get('DERAbstractString').get('superclass').get('constructor').callprop('call', var.get(u"this"))
        @Js
        def PyJs_anonymous_192_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return var.get(u"this").get('s')
        PyJs_anonymous_192_._set_name('anonymous')
        var.get(u"this").put('getString', PyJs_anonymous_192_)
        @Js
        def PyJs_anonymous_193_(newS, this, arguments, var=var):
            var = Scope({'newS':newS, 'this':this, 'arguments':arguments}, var)
            var.registers(['newS'])
            var.get(u"this").put('hTLV', var.get(u"null"))
            var.get(u"this").put('isModified', Js(True))
            var.get(u"this").put('s', var.get('newS'))
            var.get(u"this").put('hV', var.get('stohex')(var.get(u"this").get('s')))
        PyJs_anonymous_193_._set_name('anonymous')
        var.get(u"this").put('setString', PyJs_anonymous_193_)
        @Js
        def PyJs_anonymous_194_(newHexString, this, arguments, var=var):
            var = Scope({'newHexString':newHexString, 'this':this, 'arguments':arguments}, var)
            var.registers(['newHexString'])
            var.get(u"this").put('hTLV', var.get(u"null"))
            var.get(u"this").put('isModified', Js(True))
            var.get(u"this").put('s', var.get(u"null"))
            var.get(u"this").put('hV', var.get('newHexString'))
        PyJs_anonymous_194_._set_name('anonymous')
        var.get(u"this").put('setStringHex', PyJs_anonymous_194_)
        @Js
        def PyJs_anonymous_195_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return var.get(u"this").get('hV')
        PyJs_anonymous_195_._set_name('anonymous')
        var.get(u"this").put('getFreshValueHex', PyJs_anonymous_195_)
        if (var.get('params',throw=False).typeof()!=Js('undefined')):
            if (var.get('params',throw=False).typeof()==Js('string')):
                var.get(u"this").callprop('setString', var.get('params'))
            else:
                if (var.get('params').get('str').typeof()!=Js('undefined')):
                    var.get(u"this").callprop('setString', var.get('params').get('str'))
                else:
                    if (var.get('params').get('hex').typeof()!=Js('undefined')):
                        var.get(u"this").callprop('setStringHex', var.get('params').get('hex'))
    PyJs_anonymous_191_._set_name('anonymous')
    var.get('KJUR').get('asn1').put('DERAbstractString', PyJs_anonymous_191_)
    var.get('YAHOO').get('lang').callprop('extend', var.get('KJUR').get('asn1').get('DERAbstractString'), var.get('KJUR').get('asn1').get('ASN1Object'))
    @Js
    def PyJs_anonymous_196_(params, this, arguments, var=var):
        var = Scope({'params':params, 'this':this, 'arguments':arguments}, var)
        var.registers(['params'])
        var.get('KJUR').get('asn1').get('DERAbstractTime').get('superclass').get('constructor').callprop('call', var.get(u"this"))
        @Js
        def PyJs_anonymous_197_(d, this, arguments, var=var):
            var = Scope({'d':d, 'this':this, 'arguments':arguments}, var)
            var.registers(['d', 'utcDate'])
            var.put('utc', (var.get('d').callprop('getTime')+(var.get('d').callprop('getTimezoneOffset')*Js(60000.0))))
            var.put('utcDate', var.get('Date').create(var.get('utc')))
            return var.get('utcDate')
        PyJs_anonymous_197_._set_name('anonymous')
        var.get(u"this").put('localDateToUTC', PyJs_anonymous_197_)
        @Js
        def PyJs_anonymous_198_(dateObject, type, withMillis, this, arguments, var=var):
            var = Scope({'dateObject':dateObject, 'type':type, 'withMillis':withMillis, 'this':this, 'arguments':arguments}, var)
            var.registers(['dateObject', 'month', 'type', 'd', 'withMillis', 'day', 'sec', 'hour', 'pad', 'millis', 'min', 'sMillis', 'year', 's'])
            var.put('pad', var.get(u"this").get('zeroPadding'))
            var.put('d', var.get(u"this").callprop('localDateToUTC', var.get('dateObject')))
            var.put('year', var.get('String')(var.get('d').callprop('getFullYear')))
            if (var.get('type')==Js('utc')):
                var.put('year', var.get('year').callprop('substr', Js(2.0), Js(2.0)))
            var.put('month', var.get('pad')(var.get('String')((var.get('d').callprop('getMonth')+Js(1.0))), Js(2.0)))
            var.put('day', var.get('pad')(var.get('String')(var.get('d').callprop('getDate')), Js(2.0)))
            var.put('hour', var.get('pad')(var.get('String')(var.get('d').callprop('getHours')), Js(2.0)))
            var.put('min', var.get('pad')(var.get('String')(var.get('d').callprop('getMinutes')), Js(2.0)))
            var.put('sec', var.get('pad')(var.get('String')(var.get('d').callprop('getSeconds')), Js(2.0)))
            var.put('s', (((((var.get('year')+var.get('month'))+var.get('day'))+var.get('hour'))+var.get('min'))+var.get('sec')))
            if PyJsStrictEq(var.get('withMillis'),Js(True)):
                var.put('millis', var.get('d').callprop('getMilliseconds'))
                if (var.get('millis')!=Js(0.0)):
                    var.put('sMillis', var.get('pad')(var.get('String')(var.get('millis')), Js(3.0)))
                    var.put('sMillis', var.get('sMillis').callprop('replace', JsRegExp('/[0]+$/'), Js('')))
                    var.put('s', ((var.get('s')+Js('.'))+var.get('sMillis')))
            return (var.get('s')+Js('Z'))
        PyJs_anonymous_198_._set_name('anonymous')
        var.get(u"this").put('formatDate', PyJs_anonymous_198_)
        @Js
        def PyJs_anonymous_199_(s, len, this, arguments, var=var):
            var = Scope({'s':s, 'len':len, 'this':this, 'arguments':arguments}, var)
            var.registers(['len', 's'])
            if (var.get('s').get('length')>=var.get('len')):
                return var.get('s')
            return (var.get('Array').create(((var.get('len')-var.get('s').get('length'))+Js(1.0))).callprop('join', Js('0'))+var.get('s'))
        PyJs_anonymous_199_._set_name('anonymous')
        var.get(u"this").put('zeroPadding', PyJs_anonymous_199_)
        @Js
        def PyJs_anonymous_200_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return var.get(u"this").get('s')
        PyJs_anonymous_200_._set_name('anonymous')
        var.get(u"this").put('getString', PyJs_anonymous_200_)
        @Js
        def PyJs_anonymous_201_(newS, this, arguments, var=var):
            var = Scope({'newS':newS, 'this':this, 'arguments':arguments}, var)
            var.registers(['newS'])
            var.get(u"this").put('hTLV', var.get(u"null"))
            var.get(u"this").put('isModified', Js(True))
            var.get(u"this").put('s', var.get('newS'))
            var.get(u"this").put('hV', var.get('stohex')(var.get('newS')))
        PyJs_anonymous_201_._set_name('anonymous')
        var.get(u"this").put('setString', PyJs_anonymous_201_)
        @Js
        def PyJs_anonymous_202_(year, month, day, hour, min, sec, this, arguments, var=var):
            var = Scope({'year':year, 'month':month, 'day':day, 'hour':hour, 'min':min, 'sec':sec, 'this':this, 'arguments':arguments}, var)
            var.registers(['dateObject', 'month', 'day', 'sec', 'hour', 'min', 'year'])
            var.put('dateObject', var.get('Date').create(var.get('Date').callprop('UTC', var.get('year'), (var.get('month')-Js(1.0)), var.get('day'), var.get('hour'), var.get('min'), var.get('sec'), Js(0.0))))
            var.get(u"this").callprop('setByDate', var.get('dateObject'))
        PyJs_anonymous_202_._set_name('anonymous')
        var.get(u"this").put('setByDateValue', PyJs_anonymous_202_)
        @Js
        def PyJs_anonymous_203_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return var.get(u"this").get('hV')
        PyJs_anonymous_203_._set_name('anonymous')
        var.get(u"this").put('getFreshValueHex', PyJs_anonymous_203_)
    PyJs_anonymous_196_._set_name('anonymous')
    var.get('KJUR').get('asn1').put('DERAbstractTime', PyJs_anonymous_196_)
    var.get('YAHOO').get('lang').callprop('extend', var.get('KJUR').get('asn1').get('DERAbstractTime'), var.get('KJUR').get('asn1').get('ASN1Object'))
    @Js
    def PyJs_anonymous_204_(params, this, arguments, var=var):
        var = Scope({'params':params, 'this':this, 'arguments':arguments}, var)
        var.registers(['params'])
        var.get('KJUR').get('asn1').get('DERAbstractString').get('superclass').get('constructor').callprop('call', var.get(u"this"))
        @Js
        def PyJs_anonymous_205_(asn1ObjectArray, this, arguments, var=var):
            var = Scope({'asn1ObjectArray':asn1ObjectArray, 'this':this, 'arguments':arguments}, var)
            var.registers(['asn1ObjectArray'])
            var.get(u"this").put('hTLV', var.get(u"null"))
            var.get(u"this").put('isModified', Js(True))
            var.get(u"this").put('asn1Array', var.get('asn1ObjectArray'))
        PyJs_anonymous_205_._set_name('anonymous')
        var.get(u"this").put('setByASN1ObjectArray', PyJs_anonymous_205_)
        @Js
        def PyJs_anonymous_206_(asn1Object, this, arguments, var=var):
            var = Scope({'asn1Object':asn1Object, 'this':this, 'arguments':arguments}, var)
            var.registers(['asn1Object'])
            var.get(u"this").put('hTLV', var.get(u"null"))
            var.get(u"this").put('isModified', Js(True))
            var.get(u"this").get('asn1Array').callprop('push', var.get('asn1Object'))
        PyJs_anonymous_206_._set_name('anonymous')
        var.get(u"this").put('appendASN1Object', PyJs_anonymous_206_)
        var.get(u"this").put('asn1Array', var.get('Array').create())
        if (var.get('params',throw=False).typeof()!=Js('undefined')):
            if (var.get('params').get('array').typeof()!=Js('undefined')):
                var.get(u"this").put('asn1Array', var.get('params').get('array'))
    PyJs_anonymous_204_._set_name('anonymous')
    var.get('KJUR').get('asn1').put('DERAbstractStructured', PyJs_anonymous_204_)
    var.get('YAHOO').get('lang').callprop('extend', var.get('KJUR').get('asn1').get('DERAbstractStructured'), var.get('KJUR').get('asn1').get('ASN1Object'))
    @Js
    def PyJs_anonymous_207_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        var.get('KJUR').get('asn1').get('DERBoolean').get('superclass').get('constructor').callprop('call', var.get(u"this"))
        var.get(u"this").put('hT', Js('01'))
        var.get(u"this").put('hTLV', Js('0101ff'))
    PyJs_anonymous_207_._set_name('anonymous')
    var.get('KJUR').get('asn1').put('DERBoolean', PyJs_anonymous_207_)
    var.get('YAHOO').get('lang').callprop('extend', var.get('KJUR').get('asn1').get('DERBoolean'), var.get('KJUR').get('asn1').get('ASN1Object'))
    @Js
    def PyJs_anonymous_208_(params, this, arguments, var=var):
        var = Scope({'params':params, 'this':this, 'arguments':arguments}, var)
        var.registers(['params'])
        var.get('KJUR').get('asn1').get('DERInteger').get('superclass').get('constructor').callprop('call', var.get(u"this"))
        var.get(u"this").put('hT', Js('02'))
        @Js
        def PyJs_anonymous_209_(bigIntegerValue, this, arguments, var=var):
            var = Scope({'bigIntegerValue':bigIntegerValue, 'this':this, 'arguments':arguments}, var)
            var.registers(['bigIntegerValue'])
            var.get(u"this").put('hTLV', var.get(u"null"))
            var.get(u"this").put('isModified', Js(True))
            var.get(u"this").put('hV', var.get('KJUR').get('asn1').get('ASN1Util').callprop('bigIntToMinTwosComplementsHex', var.get('bigIntegerValue')))
        PyJs_anonymous_209_._set_name('anonymous')
        var.get(u"this").put('setByBigInteger', PyJs_anonymous_209_)
        @Js
        def PyJs_anonymous_210_(intValue, this, arguments, var=var):
            var = Scope({'intValue':intValue, 'this':this, 'arguments':arguments}, var)
            var.registers(['intValue', 'bi'])
            var.put('bi', var.get('BigInteger').create(var.get('String')(var.get('intValue')), Js(10.0)))
            var.get(u"this").callprop('setByBigInteger', var.get('bi'))
        PyJs_anonymous_210_._set_name('anonymous')
        var.get(u"this").put('setByInteger', PyJs_anonymous_210_)
        @Js
        def PyJs_anonymous_211_(newHexString, this, arguments, var=var):
            var = Scope({'newHexString':newHexString, 'this':this, 'arguments':arguments}, var)
            var.registers(['newHexString'])
            var.get(u"this").put('hV', var.get('newHexString'))
        PyJs_anonymous_211_._set_name('anonymous')
        var.get(u"this").put('setValueHex', PyJs_anonymous_211_)
        @Js
        def PyJs_anonymous_212_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return var.get(u"this").get('hV')
        PyJs_anonymous_212_._set_name('anonymous')
        var.get(u"this").put('getFreshValueHex', PyJs_anonymous_212_)
        if (var.get('params',throw=False).typeof()!=Js('undefined')):
            if (var.get('params').get('bigint').typeof()!=Js('undefined')):
                var.get(u"this").callprop('setByBigInteger', var.get('params').get('bigint'))
            else:
                if (var.get('params').get('int').typeof()!=Js('undefined')):
                    var.get(u"this").callprop('setByInteger', var.get('params').get('int'))
                else:
                    if (var.get('params',throw=False).typeof()==Js('number')):
                        var.get(u"this").callprop('setByInteger', var.get('params'))
                    else:
                        if (var.get('params').get('hex').typeof()!=Js('undefined')):
                            var.get(u"this").callprop('setValueHex', var.get('params').get('hex'))
    PyJs_anonymous_208_._set_name('anonymous')
    var.get('KJUR').get('asn1').put('DERInteger', PyJs_anonymous_208_)
    var.get('YAHOO').get('lang').callprop('extend', var.get('KJUR').get('asn1').get('DERInteger'), var.get('KJUR').get('asn1').get('ASN1Object'))
    @Js
    def PyJs_anonymous_213_(params, this, arguments, var=var):
        var = Scope({'params':params, 'this':this, 'arguments':arguments}, var)
        var.registers(['o', 'params'])
        if (PyJsStrictNeq(var.get('params'),var.get('undefined')) and PyJsStrictNeq(var.get('params').get('obj').typeof(),Js('undefined'))):
            var.put('o', var.get('KJUR').get('asn1').get('ASN1Util').callprop('newObject', var.get('params').get('obj')))
            var.get('params').put('hex', (Js('00')+var.get('o').callprop('getEncodedHex')))
        var.get('KJUR').get('asn1').get('DERBitString').get('superclass').get('constructor').callprop('call', var.get(u"this"))
        var.get(u"this").put('hT', Js('03'))
        @Js
        def PyJs_anonymous_214_(newHexStringIncludingUnusedBits, this, arguments, var=var):
            var = Scope({'newHexStringIncludingUnusedBits':newHexStringIncludingUnusedBits, 'this':this, 'arguments':arguments}, var)
            var.registers(['newHexStringIncludingUnusedBits'])
            var.get(u"this").put('hTLV', var.get(u"null"))
            var.get(u"this").put('isModified', Js(True))
            var.get(u"this").put('hV', var.get('newHexStringIncludingUnusedBits'))
        PyJs_anonymous_214_._set_name('anonymous')
        var.get(u"this").put('setHexValueIncludingUnusedBits', PyJs_anonymous_214_)
        @Js
        def PyJs_anonymous_215_(unusedBits, hValue, this, arguments, var=var):
            var = Scope({'unusedBits':unusedBits, 'hValue':hValue, 'this':this, 'arguments':arguments}, var)
            var.registers(['unusedBits', 'hValue', 'hUnusedBits'])
            if ((var.get('unusedBits')<Js(0.0)) or (Js(7.0)<var.get('unusedBits'))):
                PyJsTempException = JsToPyException((Js('unused bits shall be from 0 to 7: u = ')+var.get('unusedBits')))
                raise PyJsTempException
            var.put('hUnusedBits', (Js('0')+var.get('unusedBits')))
            var.get(u"this").put('hTLV', var.get(u"null"))
            var.get(u"this").put('isModified', Js(True))
            var.get(u"this").put('hV', (var.get('hUnusedBits')+var.get('hValue')))
        PyJs_anonymous_215_._set_name('anonymous')
        var.get(u"this").put('setUnusedBitsAndHexValue', PyJs_anonymous_215_)
        @Js
        def PyJs_anonymous_216_(binaryString, this, arguments, var=var):
            var = Scope({'binaryString':binaryString, 'this':this, 'arguments':arguments}, var)
            var.registers(['unusedBits', 'x', 'b', 'binaryString', 'i', 'h'])
            var.put('binaryString', var.get('binaryString').callprop('replace', JsRegExp('/0+$/'), Js('')))
            var.put('unusedBits', (Js(8.0)-(var.get('binaryString').get('length')%Js(8.0))))
            if (var.get('unusedBits')==Js(8.0)):
                var.put('unusedBits', Js(0.0))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<=var.get('unusedBits')):
                try:
                    var.put('binaryString', Js('0'), '+')
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('h', Js(''))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<(var.get('binaryString').get('length')-Js(1.0))):
                try:
                    var.put('b', var.get('binaryString').callprop('substr', var.get('i'), Js(8.0)))
                    var.put('x', var.get('parseInt')(var.get('b'), Js(2.0)).callprop('toString', Js(16.0)))
                    if (var.get('x').get('length')==Js(1.0)):
                        var.put('x', (Js('0')+var.get('x')))
                    var.put('h', var.get('x'), '+')
                finally:
                        var.put('i', Js(8.0), '+')
            var.get(u"this").put('hTLV', var.get(u"null"))
            var.get(u"this").put('isModified', Js(True))
            var.get(u"this").put('hV', ((Js('0')+var.get('unusedBits'))+var.get('h')))
        PyJs_anonymous_216_._set_name('anonymous')
        var.get(u"this").put('setByBinaryString', PyJs_anonymous_216_)
        @Js
        def PyJs_anonymous_217_(booleanArray, this, arguments, var=var):
            var = Scope({'booleanArray':booleanArray, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'booleanArray', 's'])
            var.put('s', Js(''))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('booleanArray').get('length')):
                try:
                    if (var.get('booleanArray').get(var.get('i'))==Js(True)):
                        var.put('s', Js('1'), '+')
                    else:
                        var.put('s', Js('0'), '+')
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.get(u"this").callprop('setByBinaryString', var.get('s'))
        PyJs_anonymous_217_._set_name('anonymous')
        var.get(u"this").put('setByBooleanArray', PyJs_anonymous_217_)
        @Js
        def PyJs_anonymous_218_(nLength, this, arguments, var=var):
            var = Scope({'nLength':nLength, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'a', 'nLength'])
            var.put('a', var.get('Array').create(var.get('nLength')))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('nLength')):
                try:
                    var.get('a').put(var.get('i'), Js(False))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            return var.get('a')
        PyJs_anonymous_218_._set_name('anonymous')
        var.get(u"this").put('newFalseArray', PyJs_anonymous_218_)
        @Js
        def PyJs_anonymous_219_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return var.get(u"this").get('hV')
        PyJs_anonymous_219_._set_name('anonymous')
        var.get(u"this").put('getFreshValueHex', PyJs_anonymous_219_)
        if (var.get('params',throw=False).typeof()!=Js('undefined')):
            if ((var.get('params',throw=False).typeof()==Js('string')) and var.get('params').callprop('toLowerCase').callprop('match', JsRegExp('/^[0-9a-f]+$/'))):
                var.get(u"this").callprop('setHexValueIncludingUnusedBits', var.get('params'))
            else:
                if (var.get('params').get('hex').typeof()!=Js('undefined')):
                    var.get(u"this").callprop('setHexValueIncludingUnusedBits', var.get('params').get('hex'))
                else:
                    if (var.get('params').get('bin').typeof()!=Js('undefined')):
                        var.get(u"this").callprop('setByBinaryString', var.get('params').get('bin'))
                    else:
                        if (var.get('params').get('array').typeof()!=Js('undefined')):
                            var.get(u"this").callprop('setByBooleanArray', var.get('params').get('array'))
    PyJs_anonymous_213_._set_name('anonymous')
    var.get('KJUR').get('asn1').put('DERBitString', PyJs_anonymous_213_)
    var.get('YAHOO').get('lang').callprop('extend', var.get('KJUR').get('asn1').get('DERBitString'), var.get('KJUR').get('asn1').get('ASN1Object'))
    @Js
    def PyJs_anonymous_220_(params, this, arguments, var=var):
        var = Scope({'params':params, 'this':this, 'arguments':arguments}, var)
        var.registers(['o', 'params'])
        if (PyJsStrictNeq(var.get('params'),var.get('undefined')) and PyJsStrictNeq(var.get('params').get('obj').typeof(),Js('undefined'))):
            var.put('o', var.get('KJUR').get('asn1').get('ASN1Util').callprop('newObject', var.get('params').get('obj')))
            var.get('params').put('hex', var.get('o').callprop('getEncodedHex'))
        var.get('KJUR').get('asn1').get('DEROctetString').get('superclass').get('constructor').callprop('call', var.get(u"this"), var.get('params'))
        var.get(u"this").put('hT', Js('04'))
    PyJs_anonymous_220_._set_name('anonymous')
    var.get('KJUR').get('asn1').put('DEROctetString', PyJs_anonymous_220_)
    var.get('YAHOO').get('lang').callprop('extend', var.get('KJUR').get('asn1').get('DEROctetString'), var.get('KJUR').get('asn1').get('DERAbstractString'))
    @Js
    def PyJs_anonymous_221_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers([])
        var.get('KJUR').get('asn1').get('DERNull').get('superclass').get('constructor').callprop('call', var.get(u"this"))
        var.get(u"this").put('hT', Js('05'))
        var.get(u"this").put('hTLV', Js('0500'))
    PyJs_anonymous_221_._set_name('anonymous')
    var.get('KJUR').get('asn1').put('DERNull', PyJs_anonymous_221_)
    var.get('YAHOO').get('lang').callprop('extend', var.get('KJUR').get('asn1').get('DERNull'), var.get('KJUR').get('asn1').get('ASN1Object'))
    @Js
    def PyJs_anonymous_222_(params, this, arguments, var=var):
        var = Scope({'params':params, 'this':this, 'arguments':arguments}, var)
        var.registers(['itox', 'roidtox', 'params'])
        @Js
        def PyJs_anonymous_223_(i, this, arguments, var=var):
            var = Scope({'i':i, 'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'h'])
            var.put('h', var.get('i').callprop('toString', Js(16.0)))
            if (var.get('h').get('length')==Js(1.0)):
                var.put('h', (Js('0')+var.get('h')))
            return var.get('h')
        PyJs_anonymous_223_._set_name('anonymous')
        var.put('itox', PyJs_anonymous_223_)
        @Js
        def PyJs_anonymous_224_(roid, this, arguments, var=var):
            var = Scope({'roid':roid, 'this':this, 'arguments':arguments}, var)
            var.registers(['b', 'roid', 'bPad', 'padLen', 'bi', 'b8', 'i', 'h'])
            var.put('h', Js(''))
            var.put('bi', var.get('BigInteger').create(var.get('roid'), Js(10.0)))
            var.put('b', var.get('bi').callprop('toString', Js(2.0)))
            var.put('padLen', (Js(7.0)-(var.get('b').get('length')%Js(7.0))))
            if (var.get('padLen')==Js(7.0)):
                var.put('padLen', Js(0.0))
            var.put('bPad', Js(''))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('padLen')):
                try:
                    var.put('bPad', Js('0'), '+')
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.put('b', (var.get('bPad')+var.get('b')))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<(var.get('b').get('length')-Js(1.0))):
                try:
                    var.put('b8', var.get('b').callprop('substr', var.get('i'), Js(7.0)))
                    if (var.get('i')!=(var.get('b').get('length')-Js(7.0))):
                        var.put('b8', (Js('1')+var.get('b8')))
                    var.put('h', var.get('itox')(var.get('parseInt')(var.get('b8'), Js(2.0))), '+')
                finally:
                        var.put('i', Js(7.0), '+')
            return var.get('h')
        PyJs_anonymous_224_._set_name('anonymous')
        var.put('roidtox', PyJs_anonymous_224_)
        var.get('KJUR').get('asn1').get('DERObjectIdentifier').get('superclass').get('constructor').callprop('call', var.get(u"this"))
        var.get(u"this").put('hT', Js('06'))
        @Js
        def PyJs_anonymous_225_(newHexString, this, arguments, var=var):
            var = Scope({'newHexString':newHexString, 'this':this, 'arguments':arguments}, var)
            var.registers(['newHexString'])
            var.get(u"this").put('hTLV', var.get(u"null"))
            var.get(u"this").put('isModified', Js(True))
            var.get(u"this").put('s', var.get(u"null"))
            var.get(u"this").put('hV', var.get('newHexString'))
        PyJs_anonymous_225_._set_name('anonymous')
        var.get(u"this").put('setValueHex', PyJs_anonymous_225_)
        @Js
        def PyJs_anonymous_226_(oidString, this, arguments, var=var):
            var = Scope({'oidString':oidString, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 'oidString', 'i', 'i0', 'h'])
            if var.get('oidString').callprop('match', JsRegExp('/^[0-9.]+$/')).neg():
                PyJsTempException = JsToPyException((Js('malformed oid string: ')+var.get('oidString')))
                raise PyJsTempException
            var.put('h', Js(''))
            var.put('a', var.get('oidString').callprop('split', Js('.')))
            var.put('i0', ((var.get('parseInt')(var.get('a').get('0'))*Js(40.0))+var.get('parseInt')(var.get('a').get('1'))))
            var.put('h', var.get('itox')(var.get('i0')), '+')
            var.get('a').callprop('splice', Js(0.0), Js(2.0))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('a').get('length')):
                try:
                    var.put('h', var.get('roidtox')(var.get('a').get(var.get('i'))), '+')
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.get(u"this").put('hTLV', var.get(u"null"))
            var.get(u"this").put('isModified', Js(True))
            var.get(u"this").put('s', var.get(u"null"))
            var.get(u"this").put('hV', var.get('h'))
        PyJs_anonymous_226_._set_name('anonymous')
        var.get(u"this").put('setValueOidString', PyJs_anonymous_226_)
        @Js
        def PyJs_anonymous_227_(oidName, this, arguments, var=var):
            var = Scope({'oidName':oidName, 'this':this, 'arguments':arguments}, var)
            var.registers(['oidName', 'oid'])
            var.put('oid', var.get('KJUR').get('asn1').get('x509').get('OID').callprop('name2oid', var.get('oidName')))
            if PyJsStrictNeq(var.get('oid'),Js('')):
                var.get(u"this").callprop('setValueOidString', var.get('oid'))
            else:
                PyJsTempException = JsToPyException((Js('DERObjectIdentifier oidName undefined: ')+var.get('oidName')))
                raise PyJsTempException
        PyJs_anonymous_227_._set_name('anonymous')
        var.get(u"this").put('setValueName', PyJs_anonymous_227_)
        @Js
        def PyJs_anonymous_228_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return var.get(u"this").get('hV')
        PyJs_anonymous_228_._set_name('anonymous')
        var.get(u"this").put('getFreshValueHex', PyJs_anonymous_228_)
        if PyJsStrictNeq(var.get('params'),var.get('undefined')):
            if PyJsStrictEq(var.get('params',throw=False).typeof(),Js('string')):
                if var.get('params').callprop('match', JsRegExp('/^[0-2].[0-9.]+$/')):
                    var.get(u"this").callprop('setValueOidString', var.get('params'))
                else:
                    var.get(u"this").callprop('setValueName', var.get('params'))
            else:
                if PyJsStrictNeq(var.get('params').get('oid'),var.get('undefined')):
                    var.get(u"this").callprop('setValueOidString', var.get('params').get('oid'))
                else:
                    if PyJsStrictNeq(var.get('params').get('hex'),var.get('undefined')):
                        var.get(u"this").callprop('setValueHex', var.get('params').get('hex'))
                    else:
                        if PyJsStrictNeq(var.get('params').get('name'),var.get('undefined')):
                            var.get(u"this").callprop('setValueName', var.get('params').get('name'))
    PyJs_anonymous_222_._set_name('anonymous')
    var.get('KJUR').get('asn1').put('DERObjectIdentifier', PyJs_anonymous_222_)
    var.get('YAHOO').get('lang').callprop('extend', var.get('KJUR').get('asn1').get('DERObjectIdentifier'), var.get('KJUR').get('asn1').get('ASN1Object'))
    @Js
    def PyJs_anonymous_229_(params, this, arguments, var=var):
        var = Scope({'params':params, 'this':this, 'arguments':arguments}, var)
        var.registers(['params'])
        var.get('KJUR').get('asn1').get('DEREnumerated').get('superclass').get('constructor').callprop('call', var.get(u"this"))
        var.get(u"this").put('hT', Js('0a'))
        @Js
        def PyJs_anonymous_230_(bigIntegerValue, this, arguments, var=var):
            var = Scope({'bigIntegerValue':bigIntegerValue, 'this':this, 'arguments':arguments}, var)
            var.registers(['bigIntegerValue'])
            var.get(u"this").put('hTLV', var.get(u"null"))
            var.get(u"this").put('isModified', Js(True))
            var.get(u"this").put('hV', var.get('KJUR').get('asn1').get('ASN1Util').callprop('bigIntToMinTwosComplementsHex', var.get('bigIntegerValue')))
        PyJs_anonymous_230_._set_name('anonymous')
        var.get(u"this").put('setByBigInteger', PyJs_anonymous_230_)
        @Js
        def PyJs_anonymous_231_(intValue, this, arguments, var=var):
            var = Scope({'intValue':intValue, 'this':this, 'arguments':arguments}, var)
            var.registers(['intValue', 'bi'])
            var.put('bi', var.get('BigInteger').create(var.get('String')(var.get('intValue')), Js(10.0)))
            var.get(u"this").callprop('setByBigInteger', var.get('bi'))
        PyJs_anonymous_231_._set_name('anonymous')
        var.get(u"this").put('setByInteger', PyJs_anonymous_231_)
        @Js
        def PyJs_anonymous_232_(newHexString, this, arguments, var=var):
            var = Scope({'newHexString':newHexString, 'this':this, 'arguments':arguments}, var)
            var.registers(['newHexString'])
            var.get(u"this").put('hV', var.get('newHexString'))
        PyJs_anonymous_232_._set_name('anonymous')
        var.get(u"this").put('setValueHex', PyJs_anonymous_232_)
        @Js
        def PyJs_anonymous_233_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return var.get(u"this").get('hV')
        PyJs_anonymous_233_._set_name('anonymous')
        var.get(u"this").put('getFreshValueHex', PyJs_anonymous_233_)
        if (var.get('params',throw=False).typeof()!=Js('undefined')):
            if (var.get('params').get('int').typeof()!=Js('undefined')):
                var.get(u"this").callprop('setByInteger', var.get('params').get('int'))
            else:
                if (var.get('params',throw=False).typeof()==Js('number')):
                    var.get(u"this").callprop('setByInteger', var.get('params'))
                else:
                    if (var.get('params').get('hex').typeof()!=Js('undefined')):
                        var.get(u"this").callprop('setValueHex', var.get('params').get('hex'))
    PyJs_anonymous_229_._set_name('anonymous')
    var.get('KJUR').get('asn1').put('DEREnumerated', PyJs_anonymous_229_)
    var.get('YAHOO').get('lang').callprop('extend', var.get('KJUR').get('asn1').get('DEREnumerated'), var.get('KJUR').get('asn1').get('ASN1Object'))
    @Js
    def PyJs_anonymous_234_(params, this, arguments, var=var):
        var = Scope({'params':params, 'this':this, 'arguments':arguments}, var)
        var.registers(['params'])
        var.get('KJUR').get('asn1').get('DERUTF8String').get('superclass').get('constructor').callprop('call', var.get(u"this"), var.get('params'))
        var.get(u"this").put('hT', Js('0c'))
    PyJs_anonymous_234_._set_name('anonymous')
    var.get('KJUR').get('asn1').put('DERUTF8String', PyJs_anonymous_234_)
    var.get('YAHOO').get('lang').callprop('extend', var.get('KJUR').get('asn1').get('DERUTF8String'), var.get('KJUR').get('asn1').get('DERAbstractString'))
    @Js
    def PyJs_anonymous_235_(params, this, arguments, var=var):
        var = Scope({'params':params, 'this':this, 'arguments':arguments}, var)
        var.registers(['params'])
        var.get('KJUR').get('asn1').get('DERNumericString').get('superclass').get('constructor').callprop('call', var.get(u"this"), var.get('params'))
        var.get(u"this").put('hT', Js('12'))
    PyJs_anonymous_235_._set_name('anonymous')
    var.get('KJUR').get('asn1').put('DERNumericString', PyJs_anonymous_235_)
    var.get('YAHOO').get('lang').callprop('extend', var.get('KJUR').get('asn1').get('DERNumericString'), var.get('KJUR').get('asn1').get('DERAbstractString'))
    @Js
    def PyJs_anonymous_236_(params, this, arguments, var=var):
        var = Scope({'params':params, 'this':this, 'arguments':arguments}, var)
        var.registers(['params'])
        var.get('KJUR').get('asn1').get('DERPrintableString').get('superclass').get('constructor').callprop('call', var.get(u"this"), var.get('params'))
        var.get(u"this").put('hT', Js('13'))
    PyJs_anonymous_236_._set_name('anonymous')
    var.get('KJUR').get('asn1').put('DERPrintableString', PyJs_anonymous_236_)
    var.get('YAHOO').get('lang').callprop('extend', var.get('KJUR').get('asn1').get('DERPrintableString'), var.get('KJUR').get('asn1').get('DERAbstractString'))
    @Js
    def PyJs_anonymous_237_(params, this, arguments, var=var):
        var = Scope({'params':params, 'this':this, 'arguments':arguments}, var)
        var.registers(['params'])
        var.get('KJUR').get('asn1').get('DERTeletexString').get('superclass').get('constructor').callprop('call', var.get(u"this"), var.get('params'))
        var.get(u"this").put('hT', Js('14'))
    PyJs_anonymous_237_._set_name('anonymous')
    var.get('KJUR').get('asn1').put('DERTeletexString', PyJs_anonymous_237_)
    var.get('YAHOO').get('lang').callprop('extend', var.get('KJUR').get('asn1').get('DERTeletexString'), var.get('KJUR').get('asn1').get('DERAbstractString'))
    @Js
    def PyJs_anonymous_238_(params, this, arguments, var=var):
        var = Scope({'params':params, 'this':this, 'arguments':arguments}, var)
        var.registers(['params'])
        var.get('KJUR').get('asn1').get('DERIA5String').get('superclass').get('constructor').callprop('call', var.get(u"this"), var.get('params'))
        var.get(u"this").put('hT', Js('16'))
    PyJs_anonymous_238_._set_name('anonymous')
    var.get('KJUR').get('asn1').put('DERIA5String', PyJs_anonymous_238_)
    var.get('YAHOO').get('lang').callprop('extend', var.get('KJUR').get('asn1').get('DERIA5String'), var.get('KJUR').get('asn1').get('DERAbstractString'))
    @Js
    def PyJs_anonymous_239_(params, this, arguments, var=var):
        var = Scope({'params':params, 'this':this, 'arguments':arguments}, var)
        var.registers(['params'])
        var.get('KJUR').get('asn1').get('DERUTCTime').get('superclass').get('constructor').callprop('call', var.get(u"this"), var.get('params'))
        var.get(u"this").put('hT', Js('17'))
        @Js
        def PyJs_anonymous_240_(dateObject, this, arguments, var=var):
            var = Scope({'dateObject':dateObject, 'this':this, 'arguments':arguments}, var)
            var.registers(['dateObject'])
            var.get(u"this").put('hTLV', var.get(u"null"))
            var.get(u"this").put('isModified', Js(True))
            var.get(u"this").put('date', var.get('dateObject'))
            var.get(u"this").put('s', var.get(u"this").callprop('formatDate', var.get(u"this").get('date'), Js('utc')))
            var.get(u"this").put('hV', var.get('stohex')(var.get(u"this").get('s')))
        PyJs_anonymous_240_._set_name('anonymous')
        var.get(u"this").put('setByDate', PyJs_anonymous_240_)
        @Js
        def PyJs_anonymous_241_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            if ((var.get(u"this").get('date').typeof()==Js('undefined')) and (var.get(u"this").get('s').typeof()==Js('undefined'))):
                var.get(u"this").put('date', var.get('Date').create())
                var.get(u"this").put('s', var.get(u"this").callprop('formatDate', var.get(u"this").get('date'), Js('utc')))
                var.get(u"this").put('hV', var.get('stohex')(var.get(u"this").get('s')))
            return var.get(u"this").get('hV')
        PyJs_anonymous_241_._set_name('anonymous')
        var.get(u"this").put('getFreshValueHex', PyJs_anonymous_241_)
        if PyJsStrictNeq(var.get('params'),var.get('undefined')):
            if PyJsStrictNeq(var.get('params').get('str'),var.get('undefined')):
                var.get(u"this").callprop('setString', var.get('params').get('str'))
            else:
                if ((var.get('params',throw=False).typeof()==Js('string')) and var.get('params').callprop('match', JsRegExp('/^[0-9]{12}Z$/'))):
                    var.get(u"this").callprop('setString', var.get('params'))
                else:
                    if PyJsStrictNeq(var.get('params').get('hex'),var.get('undefined')):
                        var.get(u"this").callprop('setStringHex', var.get('params').get('hex'))
                    else:
                        if PyJsStrictNeq(var.get('params').get('date'),var.get('undefined')):
                            var.get(u"this").callprop('setByDate', var.get('params').get('date'))
    PyJs_anonymous_239_._set_name('anonymous')
    var.get('KJUR').get('asn1').put('DERUTCTime', PyJs_anonymous_239_)
    var.get('YAHOO').get('lang').callprop('extend', var.get('KJUR').get('asn1').get('DERUTCTime'), var.get('KJUR').get('asn1').get('DERAbstractTime'))
    @Js
    def PyJs_anonymous_242_(params, this, arguments, var=var):
        var = Scope({'params':params, 'this':this, 'arguments':arguments}, var)
        var.registers(['params'])
        var.get('KJUR').get('asn1').get('DERGeneralizedTime').get('superclass').get('constructor').callprop('call', var.get(u"this"), var.get('params'))
        var.get(u"this").put('hT', Js('18'))
        var.get(u"this").put('withMillis', Js(False))
        @Js
        def PyJs_anonymous_243_(dateObject, this, arguments, var=var):
            var = Scope({'dateObject':dateObject, 'this':this, 'arguments':arguments}, var)
            var.registers(['dateObject'])
            var.get(u"this").put('hTLV', var.get(u"null"))
            var.get(u"this").put('isModified', Js(True))
            var.get(u"this").put('date', var.get('dateObject'))
            var.get(u"this").put('s', var.get(u"this").callprop('formatDate', var.get(u"this").get('date'), Js('gen'), var.get(u"this").get('withMillis')))
            var.get(u"this").put('hV', var.get('stohex')(var.get(u"this").get('s')))
        PyJs_anonymous_243_._set_name('anonymous')
        var.get(u"this").put('setByDate', PyJs_anonymous_243_)
        @Js
        def PyJs_anonymous_244_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            if (PyJsStrictEq(var.get(u"this").get('date'),var.get('undefined')) and PyJsStrictEq(var.get(u"this").get('s'),var.get('undefined'))):
                var.get(u"this").put('date', var.get('Date').create())
                var.get(u"this").put('s', var.get(u"this").callprop('formatDate', var.get(u"this").get('date'), Js('gen'), var.get(u"this").get('withMillis')))
                var.get(u"this").put('hV', var.get('stohex')(var.get(u"this").get('s')))
            return var.get(u"this").get('hV')
        PyJs_anonymous_244_._set_name('anonymous')
        var.get(u"this").put('getFreshValueHex', PyJs_anonymous_244_)
        if PyJsStrictNeq(var.get('params'),var.get('undefined')):
            if PyJsStrictNeq(var.get('params').get('str'),var.get('undefined')):
                var.get(u"this").callprop('setString', var.get('params').get('str'))
            else:
                if ((var.get('params',throw=False).typeof()==Js('string')) and var.get('params').callprop('match', JsRegExp('/^[0-9]{14}Z$/'))):
                    var.get(u"this").callprop('setString', var.get('params'))
                else:
                    if PyJsStrictNeq(var.get('params').get('hex'),var.get('undefined')):
                        var.get(u"this").callprop('setStringHex', var.get('params').get('hex'))
                    else:
                        if PyJsStrictNeq(var.get('params').get('date'),var.get('undefined')):
                            var.get(u"this").callprop('setByDate', var.get('params').get('date'))
            if PyJsStrictEq(var.get('params').get('millis'),Js(True)):
                var.get(u"this").put('withMillis', Js(True))
    PyJs_anonymous_242_._set_name('anonymous')
    var.get('KJUR').get('asn1').put('DERGeneralizedTime', PyJs_anonymous_242_)
    var.get('YAHOO').get('lang').callprop('extend', var.get('KJUR').get('asn1').get('DERGeneralizedTime'), var.get('KJUR').get('asn1').get('DERAbstractTime'))
    @Js
    def PyJs_anonymous_245_(params, this, arguments, var=var):
        var = Scope({'params':params, 'this':this, 'arguments':arguments}, var)
        var.registers(['params'])
        var.get('KJUR').get('asn1').get('DERSequence').get('superclass').get('constructor').callprop('call', var.get(u"this"), var.get('params'))
        var.get(u"this").put('hT', Js('30'))
        @Js
        def PyJs_anonymous_246_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'asn1Obj', 'h'])
            var.put('h', Js(''))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get(u"this").get('asn1Array').get('length')):
                try:
                    var.put('asn1Obj', var.get(u"this").get('asn1Array').get(var.get('i')))
                    var.put('h', var.get('asn1Obj').callprop('getEncodedHex'), '+')
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            var.get(u"this").put('hV', var.get('h'))
            return var.get(u"this").get('hV')
        PyJs_anonymous_246_._set_name('anonymous')
        var.get(u"this").put('getFreshValueHex', PyJs_anonymous_246_)
    PyJs_anonymous_245_._set_name('anonymous')
    var.get('KJUR').get('asn1').put('DERSequence', PyJs_anonymous_245_)
    var.get('YAHOO').get('lang').callprop('extend', var.get('KJUR').get('asn1').get('DERSequence'), var.get('KJUR').get('asn1').get('DERAbstractStructured'))
    @Js
    def PyJs_anonymous_247_(params, this, arguments, var=var):
        var = Scope({'params':params, 'this':this, 'arguments':arguments}, var)
        var.registers(['params'])
        var.get('KJUR').get('asn1').get('DERSet').get('superclass').get('constructor').callprop('call', var.get(u"this"), var.get('params'))
        var.get(u"this").put('hT', Js('31'))
        var.get(u"this").put('sortFlag', Js(True))
        @Js
        def PyJs_anonymous_248_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['i', 'a', 'asn1Obj'])
            var.put('a', var.get('Array').create())
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get(u"this").get('asn1Array').get('length')):
                try:
                    var.put('asn1Obj', var.get(u"this").get('asn1Array').get(var.get('i')))
                    var.get('a').callprop('push', var.get('asn1Obj').callprop('getEncodedHex'))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            if (var.get(u"this").get('sortFlag')==Js(True)):
                var.get('a').callprop('sort')
            var.get(u"this").put('hV', var.get('a').callprop('join', Js('')))
            return var.get(u"this").get('hV')
        PyJs_anonymous_248_._set_name('anonymous')
        var.get(u"this").put('getFreshValueHex', PyJs_anonymous_248_)
        if (var.get('params',throw=False).typeof()!=Js('undefined')):
            if ((var.get('params').get('sortflag').typeof()!=Js('undefined')) and (var.get('params').get('sortflag')==Js(False))):
                var.get(u"this").put('sortFlag', Js(False))
    PyJs_anonymous_247_._set_name('anonymous')
    var.get('KJUR').get('asn1').put('DERSet', PyJs_anonymous_247_)
    var.get('YAHOO').get('lang').callprop('extend', var.get('KJUR').get('asn1').get('DERSet'), var.get('KJUR').get('asn1').get('DERAbstractStructured'))
    @Js
    def PyJs_anonymous_249_(params, this, arguments, var=var):
        var = Scope({'params':params, 'this':this, 'arguments':arguments}, var)
        var.registers(['params'])
        var.get('KJUR').get('asn1').get('DERTaggedObject').get('superclass').get('constructor').callprop('call', var.get(u"this"))
        var.get(u"this").put('hT', Js('a0'))
        var.get(u"this").put('hV', Js(''))
        var.get(u"this").put('isExplicit', Js(True))
        var.get(u"this").put('asn1Object', var.get(u"null"))
        @Js
        def PyJs_anonymous_250_(isExplicitFlag, tagNoHex, asn1Object, this, arguments, var=var):
            var = Scope({'isExplicitFlag':isExplicitFlag, 'tagNoHex':tagNoHex, 'asn1Object':asn1Object, 'this':this, 'arguments':arguments}, var)
            var.registers(['isExplicitFlag', 'tagNoHex', 'asn1Object'])
            var.get(u"this").put('hT', var.get('tagNoHex'))
            var.get(u"this").put('isExplicit', var.get('isExplicitFlag'))
            var.get(u"this").put('asn1Object', var.get('asn1Object'))
            if var.get(u"this").get('isExplicit'):
                var.get(u"this").put('hV', var.get(u"this").get('asn1Object').callprop('getEncodedHex'))
                var.get(u"this").put('hTLV', var.get(u"null"))
                var.get(u"this").put('isModified', Js(True))
            else:
                var.get(u"this").put('hV', var.get(u"null"))
                var.get(u"this").put('hTLV', var.get('asn1Object').callprop('getEncodedHex'))
                var.get(u"this").put('hTLV', var.get(u"this").get('hTLV').callprop('replace', JsRegExp('/^../'), var.get('tagNoHex')))
                var.get(u"this").put('isModified', Js(False))
        PyJs_anonymous_250_._set_name('anonymous')
        var.get(u"this").put('setASN1Object', PyJs_anonymous_250_)
        @Js
        def PyJs_anonymous_251_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return var.get(u"this").get('hV')
        PyJs_anonymous_251_._set_name('anonymous')
        var.get(u"this").put('getFreshValueHex', PyJs_anonymous_251_)
        if (var.get('params',throw=False).typeof()!=Js('undefined')):
            if (var.get('params').get('tag').typeof()!=Js('undefined')):
                var.get(u"this").put('hT', var.get('params').get('tag'))
            if (var.get('params').get('explicit').typeof()!=Js('undefined')):
                var.get(u"this").put('isExplicit', var.get('params').get('explicit'))
            if (var.get('params').get('obj').typeof()!=Js('undefined')):
                var.get(u"this").put('asn1Object', var.get('params').get('obj'))
                var.get(u"this").callprop('setASN1Object', var.get(u"this").get('isExplicit'), var.get(u"this").get('hT'), var.get(u"this").get('asn1Object'))
    PyJs_anonymous_249_._set_name('anonymous')
    var.get('KJUR').get('asn1').put('DERTaggedObject', PyJs_anonymous_249_)
    var.get('YAHOO').get('lang').callprop('extend', var.get('KJUR').get('asn1').get('DERTaggedObject'), var.get('KJUR').get('asn1').get('ASN1Object'))
    @Js
    def PyJs_anonymous_252_(_super, this, arguments, var=var):
        var = Scope({'_super':_super, 'this':this, 'arguments':arguments}, var)
        var.registers(['_super', 'JSEncryptRSAKey'])
        @Js
        def PyJsHoisted_JSEncryptRSAKey_(key, this, arguments, var=var):
            var = Scope({'key':key, 'this':this, 'arguments':arguments}, var)
            var.registers(['key', '_this'])
            var.put('_this', (var.get('_super').callprop('call', var.get(u"this")) or var.get(u"this")))
            if var.get('key'):
                if PyJsStrictEq(var.get('key',throw=False).typeof(),Js('string')):
                    var.get('_this').callprop('parseKey', var.get('key'))
                else:
                    if (var.get('JSEncryptRSAKey').callprop('hasPrivateKeyProperty', var.get('key')) or var.get('JSEncryptRSAKey').callprop('hasPublicKeyProperty', var.get('key'))):
                        var.get('_this').callprop('parsePropertiesFrom', var.get('key'))
            return var.get('_this')
        PyJsHoisted_JSEncryptRSAKey_.func_name = 'JSEncryptRSAKey'
        var.put('JSEncryptRSAKey', PyJsHoisted_JSEncryptRSAKey_)
        var.get('__extends')(var.get('JSEncryptRSAKey'), var.get('_super'))
        pass
        @Js
        def PyJs_anonymous_253_(pem, this, arguments, var=var):
            var = Scope({'pem':pem, 'this':this, 'arguments':arguments}, var)
            var.registers(['prime1', 'modulus', 'coefficient', 'reHex', 'public_exponent', 'der', 'asn1', 'exponent2', 'exponent1', 'prime2', 'bit_string', 'sequence', 'pem', 'private_exponent'])
            try:
                var.put('modulus', Js(0.0))
                var.put('public_exponent', Js(0.0))
                var.put('reHex', JsRegExp('/^\\s*(?:[0-9A-Fa-f][0-9A-Fa-f]\\s*)+$/'))
                var.put('der', (var.get('Hex').callprop('decode', var.get('pem')) if var.get('reHex').callprop('test', var.get('pem')) else var.get('Base64').callprop('unarmor', var.get('pem'))))
                var.put('asn1', var.get('ASN1').callprop('decode', var.get('der')))
                if PyJsStrictEq(var.get('asn1').get('sub').get('length'),Js(3.0)):
                    var.put('asn1', var.get('asn1').get('sub').get('2').get('sub').get('0'))
                if PyJsStrictEq(var.get('asn1').get('sub').get('length'),Js(9.0)):
                    var.put('modulus', var.get('asn1').get('sub').get('1').callprop('getHexStringValue'))
                    var.get(u"this").put('n', var.get('parseBigInt')(var.get('modulus'), Js(16.0)))
                    var.put('public_exponent', var.get('asn1').get('sub').get('2').callprop('getHexStringValue'))
                    var.get(u"this").put('e', var.get('parseInt')(var.get('public_exponent'), Js(16.0)))
                    var.put('private_exponent', var.get('asn1').get('sub').get('3').callprop('getHexStringValue'))
                    var.get(u"this").put('d', var.get('parseBigInt')(var.get('private_exponent'), Js(16.0)))
                    var.put('prime1', var.get('asn1').get('sub').get('4').callprop('getHexStringValue'))
                    var.get(u"this").put('p', var.get('parseBigInt')(var.get('prime1'), Js(16.0)))
                    var.put('prime2', var.get('asn1').get('sub').get('5').callprop('getHexStringValue'))
                    var.get(u"this").put('q', var.get('parseBigInt')(var.get('prime2'), Js(16.0)))
                    var.put('exponent1', var.get('asn1').get('sub').get('6').callprop('getHexStringValue'))
                    var.get(u"this").put('dmp1', var.get('parseBigInt')(var.get('exponent1'), Js(16.0)))
                    var.put('exponent2', var.get('asn1').get('sub').get('7').callprop('getHexStringValue'))
                    var.get(u"this").put('dmq1', var.get('parseBigInt')(var.get('exponent2'), Js(16.0)))
                    var.put('coefficient', var.get('asn1').get('sub').get('8').callprop('getHexStringValue'))
                    var.get(u"this").put('coeff', var.get('parseBigInt')(var.get('coefficient'), Js(16.0)))
                else:
                    if PyJsStrictEq(var.get('asn1').get('sub').get('length'),Js(2.0)):
                        var.put('bit_string', var.get('asn1').get('sub').get('1'))
                        var.put('sequence', var.get('bit_string').get('sub').get('0'))
                        var.put('modulus', var.get('sequence').get('sub').get('0').callprop('getHexStringValue'))
                        var.get(u"this").put('n', var.get('parseBigInt')(var.get('modulus'), Js(16.0)))
                        var.put('public_exponent', var.get('sequence').get('sub').get('1').callprop('getHexStringValue'))
                        var.get(u"this").put('e', var.get('parseInt')(var.get('public_exponent'), Js(16.0)))
                    else:
                        return Js(False)
                return Js(True)
            except PyJsException as PyJsTempException:
                PyJsHolder_6578_47046133 = var.own.get('ex')
                var.force_own_put('ex', PyExceptionToJs(PyJsTempException))
                try:
                    return Js(False)
                finally:
                    if PyJsHolder_6578_47046133 is not None:
                        var.own['ex'] = PyJsHolder_6578_47046133
                    else:
                        del var.own['ex']
                    del PyJsHolder_6578_47046133
        PyJs_anonymous_253_._set_name('anonymous')
        var.get('JSEncryptRSAKey').get('prototype').put('parseKey', PyJs_anonymous_253_)
        @Js
        def PyJs_anonymous_254_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['seq', 'options'])
            var.put('options', Js({'array':Js([var.get('KJUR').get('asn1').get('DERInteger').create(Js({'int':Js(0.0)})), var.get('KJUR').get('asn1').get('DERInteger').create(Js({'bigint':var.get(u"this").get('n')})), var.get('KJUR').get('asn1').get('DERInteger').create(Js({'int':var.get(u"this").get('e')})), var.get('KJUR').get('asn1').get('DERInteger').create(Js({'bigint':var.get(u"this").get('d')})), var.get('KJUR').get('asn1').get('DERInteger').create(Js({'bigint':var.get(u"this").get('p')})), var.get('KJUR').get('asn1').get('DERInteger').create(Js({'bigint':var.get(u"this").get('q')})), var.get('KJUR').get('asn1').get('DERInteger').create(Js({'bigint':var.get(u"this").get('dmp1')})), var.get('KJUR').get('asn1').get('DERInteger').create(Js({'bigint':var.get(u"this").get('dmq1')})), var.get('KJUR').get('asn1').get('DERInteger').create(Js({'bigint':var.get(u"this").get('coeff')}))])}))
            var.put('seq', var.get('KJUR').get('asn1').get('DERSequence').create(var.get('options')))
            return var.get('seq').callprop('getEncodedHex')
        PyJs_anonymous_254_._set_name('anonymous')
        var.get('JSEncryptRSAKey').get('prototype').put('getPrivateBaseKey', PyJs_anonymous_254_)
        @Js
        def PyJs_anonymous_255_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return var.get('hex2b64')(var.get(u"this").callprop('getPrivateBaseKey'))
        PyJs_anonymous_255_._set_name('anonymous')
        var.get('JSEncryptRSAKey').get('prototype').put('getPrivateBaseKeyB64', PyJs_anonymous_255_)
        @Js
        def PyJs_anonymous_256_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['second_sequence', 'bit_string', 'seq', 'first_sequence'])
            var.put('first_sequence', var.get('KJUR').get('asn1').get('DERSequence').create(Js({'array':Js([var.get('KJUR').get('asn1').get('DERObjectIdentifier').create(Js({'oid':Js('1.2.840.113549.1.1.1')})), var.get('KJUR').get('asn1').get('DERNull').create()])})))
            var.put('second_sequence', var.get('KJUR').get('asn1').get('DERSequence').create(Js({'array':Js([var.get('KJUR').get('asn1').get('DERInteger').create(Js({'bigint':var.get(u"this").get('n')})), var.get('KJUR').get('asn1').get('DERInteger').create(Js({'int':var.get(u"this").get('e')}))])})))
            var.put('bit_string', var.get('KJUR').get('asn1').get('DERBitString').create(Js({'hex':(Js('00')+var.get('second_sequence').callprop('getEncodedHex'))})))
            var.put('seq', var.get('KJUR').get('asn1').get('DERSequence').create(Js({'array':Js([var.get('first_sequence'), var.get('bit_string')])})))
            return var.get('seq').callprop('getEncodedHex')
        PyJs_anonymous_256_._set_name('anonymous')
        var.get('JSEncryptRSAKey').get('prototype').put('getPublicBaseKey', PyJs_anonymous_256_)
        @Js
        def PyJs_anonymous_257_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return var.get('hex2b64')(var.get(u"this").callprop('getPublicBaseKey'))
        PyJs_anonymous_257_._set_name('anonymous')
        var.get('JSEncryptRSAKey').get('prototype').put('getPublicBaseKeyB64', PyJs_anonymous_257_)
        @Js
        def PyJs_anonymous_258_(str, width, this, arguments, var=var):
            var = Scope({'str':str, 'width':width, 'this':this, 'arguments':arguments}, var)
            var.registers(['width', 'regex', 'str'])
            var.put('width', (var.get('width') or Js(64.0)))
            if var.get('str').neg():
                return var.get('str')
            var.put('regex', ((((Js('(.{1,')+var.get('width'))+Js('})( +|$\n?)|(.{1,'))+var.get('width'))+Js('})')))
            return var.get('str').callprop('match', var.get('RegExp')(var.get('regex'), Js('g'))).callprop('join', Js('\n'))
        PyJs_anonymous_258_._set_name('anonymous')
        var.get('JSEncryptRSAKey').put('wordwrap', PyJs_anonymous_258_)
        @Js
        def PyJs_anonymous_259_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['key'])
            var.put('key', Js('-----BEGIN RSA PRIVATE KEY-----\n'))
            var.put('key', (var.get('JSEncryptRSAKey').callprop('wordwrap', var.get(u"this").callprop('getPrivateBaseKeyB64'))+Js('\n')), '+')
            var.put('key', Js('-----END RSA PRIVATE KEY-----'), '+')
            return var.get('key')
        PyJs_anonymous_259_._set_name('anonymous')
        var.get('JSEncryptRSAKey').get('prototype').put('getPrivateKey', PyJs_anonymous_259_)
        @Js
        def PyJs_anonymous_260_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers(['key'])
            var.put('key', Js('-----BEGIN PUBLIC KEY-----\n'))
            var.put('key', (var.get('JSEncryptRSAKey').callprop('wordwrap', var.get(u"this").callprop('getPublicBaseKeyB64'))+Js('\n')), '+')
            var.put('key', Js('-----END PUBLIC KEY-----'), '+')
            return var.get('key')
        PyJs_anonymous_260_._set_name('anonymous')
        var.get('JSEncryptRSAKey').get('prototype').put('getPublicKey', PyJs_anonymous_260_)
        @Js
        def PyJs_anonymous_261_(obj, this, arguments, var=var):
            var = Scope({'obj':obj, 'this':this, 'arguments':arguments}, var)
            var.registers(['obj'])
            var.put('obj', (var.get('obj') or Js({})))
            return (var.get('obj').callprop('hasOwnProperty', Js('n')) and var.get('obj').callprop('hasOwnProperty', Js('e')))
        PyJs_anonymous_261_._set_name('anonymous')
        var.get('JSEncryptRSAKey').put('hasPublicKeyProperty', PyJs_anonymous_261_)
        @Js
        def PyJs_anonymous_262_(obj, this, arguments, var=var):
            var = Scope({'obj':obj, 'this':this, 'arguments':arguments}, var)
            var.registers(['obj'])
            var.put('obj', (var.get('obj') or Js({})))
            def PyJs_LONG_263_(var=var):
                return (((((((var.get('obj').callprop('hasOwnProperty', Js('n')) and var.get('obj').callprop('hasOwnProperty', Js('e'))) and var.get('obj').callprop('hasOwnProperty', Js('d'))) and var.get('obj').callprop('hasOwnProperty', Js('p'))) and var.get('obj').callprop('hasOwnProperty', Js('q'))) and var.get('obj').callprop('hasOwnProperty', Js('dmp1'))) and var.get('obj').callprop('hasOwnProperty', Js('dmq1'))) and var.get('obj').callprop('hasOwnProperty', Js('coeff')))
            return PyJs_LONG_263_()
        PyJs_anonymous_262_._set_name('anonymous')
        var.get('JSEncryptRSAKey').put('hasPrivateKeyProperty', PyJs_anonymous_262_)
        @Js
        def PyJs_anonymous_264_(obj, this, arguments, var=var):
            var = Scope({'obj':obj, 'this':this, 'arguments':arguments}, var)
            var.registers(['obj'])
            var.get(u"this").put('n', var.get('obj').get('n'))
            var.get(u"this").put('e', var.get('obj').get('e'))
            if var.get('obj').callprop('hasOwnProperty', Js('d')):
                var.get(u"this").put('d', var.get('obj').get('d'))
                var.get(u"this").put('p', var.get('obj').get('p'))
                var.get(u"this").put('q', var.get('obj').get('q'))
                var.get(u"this").put('dmp1', var.get('obj').get('dmp1'))
                var.get(u"this").put('dmq1', var.get('obj').get('dmq1'))
                var.get(u"this").put('coeff', var.get('obj').get('coeff'))
        PyJs_anonymous_264_._set_name('anonymous')
        var.get('JSEncryptRSAKey').get('prototype').put('parsePropertiesFrom', PyJs_anonymous_264_)
        return var.get('JSEncryptRSAKey')
    PyJs_anonymous_252_._set_name('anonymous')
    var.put('JSEncryptRSAKey', PyJs_anonymous_252_(var.get('RSAKey')))
    @Js
    def PyJs_anonymous_265_(this, arguments, var=var):
        var = Scope({'this':this, 'arguments':arguments}, var)
        var.registers(['JSEncrypt'])
        @Js
        def PyJsHoisted_JSEncrypt_(options, this, arguments, var=var):
            var = Scope({'options':options, 'this':this, 'arguments':arguments}, var)
            var.registers(['options'])
            var.put('options', (var.get('options') or Js({})))
            var.get(u"this").put('default_key_size', (var.get('parseInt')(var.get('options').get('default_key_size'), Js(10.0)) or Js(1024.0)))
            var.get(u"this").put('default_public_exponent', (var.get('options').get('default_public_exponent') or Js('010001')))
            var.get(u"this").put('log', (var.get('options').get('log') or Js(False)))
            var.get(u"this").put('key', var.get(u"null"))
        PyJsHoisted_JSEncrypt_.func_name = 'JSEncrypt'
        var.put('JSEncrypt', PyJsHoisted_JSEncrypt_)
        pass
        @Js
        def PyJs_anonymous_266_(key, this, arguments, var=var):
            var = Scope({'key':key, 'this':this, 'arguments':arguments}, var)
            var.registers(['key'])
            if (var.get(u"this").get('log') and var.get(u"this").get('key')):
                var.get('console').callprop('warn', Js('A key was already set, overriding existing.'))
            var.get(u"this").put('key', var.get('JSEncryptRSAKey').create(var.get('key')))
        PyJs_anonymous_266_._set_name('anonymous')
        var.get('JSEncrypt').get('prototype').put('setKey', PyJs_anonymous_266_)
        @Js
        def PyJs_anonymous_267_(privkey, this, arguments, var=var):
            var = Scope({'privkey':privkey, 'this':this, 'arguments':arguments}, var)
            var.registers(['privkey'])
            var.get(u"this").callprop('setKey', var.get('privkey'))
        PyJs_anonymous_267_._set_name('anonymous')
        var.get('JSEncrypt').get('prototype').put('setPrivateKey', PyJs_anonymous_267_)
        @Js
        def PyJs_anonymous_268_(pubkey, this, arguments, var=var):
            var = Scope({'pubkey':pubkey, 'this':this, 'arguments':arguments}, var)
            var.registers(['pubkey'])
            var.get(u"this").callprop('setKey', var.get('pubkey'))
        PyJs_anonymous_268_._set_name('anonymous')
        var.get('JSEncrypt').get('prototype').put('setPublicKey', PyJs_anonymous_268_)
        @Js
        def PyJs_anonymous_269_(str, this, arguments, var=var):
            var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
            var.registers(['str'])
            try:
                return var.get(u"this").callprop('getKey').callprop('decrypt', var.get('b64tohex')(var.get('str')))
            except PyJsException as PyJsTempException:
                PyJsHolder_6578_1826673 = var.own.get('ex')
                var.force_own_put('ex', PyExceptionToJs(PyJsTempException))
                try:
                    return Js(False)
                finally:
                    if PyJsHolder_6578_1826673 is not None:
                        var.own['ex'] = PyJsHolder_6578_1826673
                    else:
                        del var.own['ex']
                    del PyJsHolder_6578_1826673
        PyJs_anonymous_269_._set_name('anonymous')
        var.get('JSEncrypt').get('prototype').put('decrypt', PyJs_anonymous_269_)
        @Js
        def PyJs_anonymous_270_(str, this, arguments, var=var):
            var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
            var.registers(['str'])
            try:
                return var.get('hex2b64')(var.get(u"this").callprop('getKey').callprop('encrypt', var.get('str')))
            except PyJsException as PyJsTempException:
                PyJsHolder_6578_73296482 = var.own.get('ex')
                var.force_own_put('ex', PyExceptionToJs(PyJsTempException))
                try:
                    return Js(False)
                finally:
                    if PyJsHolder_6578_73296482 is not None:
                        var.own['ex'] = PyJsHolder_6578_73296482
                    else:
                        del var.own['ex']
                    del PyJsHolder_6578_73296482
        PyJs_anonymous_270_._set_name('anonymous')
        var.get('JSEncrypt').get('prototype').put('encrypt', PyJs_anonymous_270_)
        @Js
        def PyJs_anonymous_271_(str, this, arguments, var=var):
            var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
            var.registers(['encrypted', 'count', 'reg', 'uncrypted', 'str'])
            try:
                var.put('encrypted', (var.get(u"this").callprop('getKey').callprop('encryptLong', var.get('str')) or Js('')))
                var.put('uncrypted', (var.get(u"this").callprop('getKey').callprop('decryptLong', var.get('encrypted')) or Js('')))
                var.put('count', Js(0.0))
                var.put('reg', JsRegExp('/null$/g'))
                while var.get('reg').callprop('test', var.get('uncrypted')):
                    (var.put('count',Js(var.get('count').to_number())+Js(1))-Js(1))
                    var.put('encrypted', (var.get(u"this").callprop('getKey').callprop('encryptLong', var.get('str')) or Js('')))
                    var.put('uncrypted', (var.get(u"this").callprop('getKey').callprop('decryptLong', var.get('encrypted')) or Js('')))
                    if (var.get('count')>Js(10.0)):
                        break
                return var.get('encrypted')
            except PyJsException as PyJsTempException:
                PyJsHolder_6578_87109125 = var.own.get('ex')
                var.force_own_put('ex', PyExceptionToJs(PyJsTempException))
                try:
                    return Js(False)
                finally:
                    if PyJsHolder_6578_87109125 is not None:
                        var.own['ex'] = PyJsHolder_6578_87109125
                    else:
                        del var.own['ex']
                    del PyJsHolder_6578_87109125
        PyJs_anonymous_271_._set_name('anonymous')
        var.get('JSEncrypt').get('prototype').put('encryptLong', PyJs_anonymous_271_)
        @Js
        def PyJs_anonymous_272_(str, this, arguments, var=var):
            var = Scope({'str':str, 'this':this, 'arguments':arguments}, var)
            var.registers(['str'])
            try:
                return var.get(u"this").callprop('getKey').callprop('decryptLong', var.get('str'))
            except PyJsException as PyJsTempException:
                PyJsHolder_6578_17463882 = var.own.get('ex')
                var.force_own_put('ex', PyExceptionToJs(PyJsTempException))
                try:
                    return Js(False)
                finally:
                    if PyJsHolder_6578_17463882 is not None:
                        var.own['ex'] = PyJsHolder_6578_17463882
                    else:
                        del var.own['ex']
                    del PyJsHolder_6578_17463882
        PyJs_anonymous_272_._set_name('anonymous')
        var.get('JSEncrypt').get('prototype').put('decryptLong', PyJs_anonymous_272_)
        @Js
        def PyJs_anonymous_273_(str, digestMethod, digestName, this, arguments, var=var):
            var = Scope({'str':str, 'digestMethod':digestMethod, 'digestName':digestName, 'this':this, 'arguments':arguments}, var)
            var.registers(['str', 'digestName', 'digestMethod'])
            try:
                return var.get('hex2b64')(var.get(u"this").callprop('getKey').callprop('sign', var.get('str'), var.get('digestMethod'), var.get('digestName')))
            except PyJsException as PyJsTempException:
                PyJsHolder_6578_66656626 = var.own.get('ex')
                var.force_own_put('ex', PyExceptionToJs(PyJsTempException))
                try:
                    return Js(False)
                finally:
                    if PyJsHolder_6578_66656626 is not None:
                        var.own['ex'] = PyJsHolder_6578_66656626
                    else:
                        del var.own['ex']
                    del PyJsHolder_6578_66656626
        PyJs_anonymous_273_._set_name('anonymous')
        var.get('JSEncrypt').get('prototype').put('sign', PyJs_anonymous_273_)
        @Js
        def PyJs_anonymous_274_(str, signature, digestMethod, this, arguments, var=var):
            var = Scope({'str':str, 'signature':signature, 'digestMethod':digestMethod, 'this':this, 'arguments':arguments}, var)
            var.registers(['digestMethod', 'str', 'signature'])
            try:
                return var.get(u"this").callprop('getKey').callprop('verify', var.get('str'), var.get('b64tohex')(var.get('signature')), var.get('digestMethod'))
            except PyJsException as PyJsTempException:
                PyJsHolder_6578_69749140 = var.own.get('ex')
                var.force_own_put('ex', PyExceptionToJs(PyJsTempException))
                try:
                    return Js(False)
                finally:
                    if PyJsHolder_6578_69749140 is not None:
                        var.own['ex'] = PyJsHolder_6578_69749140
                    else:
                        del var.own['ex']
                    del PyJsHolder_6578_69749140
        PyJs_anonymous_274_._set_name('anonymous')
        var.get('JSEncrypt').get('prototype').put('verify', PyJs_anonymous_274_)
        @Js
        def PyJs_anonymous_275_(cb, this, arguments, var=var):
            var = Scope({'cb':cb, 'this':this, 'arguments':arguments}, var)
            var.registers(['cb'])
            if var.get(u"this").get('key').neg():
                var.get(u"this").put('key', var.get('JSEncryptRSAKey').create())
                if (var.get('cb') and PyJsStrictEq(Js({}).get('toString').callprop('call', var.get('cb')),Js('[object Function]'))):
                    var.get(u"this").get('key').callprop('generateAsync', var.get(u"this").get('default_key_size'), var.get(u"this").get('default_public_exponent'), var.get('cb'))
                    return var.get('undefined')
                var.get(u"this").get('key').callprop('generate', var.get(u"this").get('default_key_size'), var.get(u"this").get('default_public_exponent'))
            return var.get(u"this").get('key')
        PyJs_anonymous_275_._set_name('anonymous')
        var.get('JSEncrypt').get('prototype').put('getKey', PyJs_anonymous_275_)
        @Js
        def PyJs_anonymous_276_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return var.get(u"this").callprop('getKey').callprop('getPrivateKey')
        PyJs_anonymous_276_._set_name('anonymous')
        var.get('JSEncrypt').get('prototype').put('getPrivateKey', PyJs_anonymous_276_)
        @Js
        def PyJs_anonymous_277_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return var.get(u"this").callprop('getKey').callprop('getPrivateBaseKeyB64')
        PyJs_anonymous_277_._set_name('anonymous')
        var.get('JSEncrypt').get('prototype').put('getPrivateKeyB64', PyJs_anonymous_277_)
        @Js
        def PyJs_anonymous_278_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return var.get(u"this").callprop('getKey').callprop('getPublicKey')
        PyJs_anonymous_278_._set_name('anonymous')
        var.get('JSEncrypt').get('prototype').put('getPublicKey', PyJs_anonymous_278_)
        @Js
        def PyJs_anonymous_279_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            return var.get(u"this").callprop('getKey').callprop('getPublicBaseKeyB64')
        PyJs_anonymous_279_._set_name('anonymous')
        var.get('JSEncrypt').get('prototype').put('getPublicKeyB64', PyJs_anonymous_279_)
        var.get('JSEncrypt').put('version', Js('3.1.2'))
        return var.get('JSEncrypt')
    PyJs_anonymous_265_._set_name('anonymous')
    var.put('JSEncrypt', PyJs_anonymous_265_())
    var.get('window').put('JSEncrypt', var.get('JSEncrypt'))
    var.get('exports').put('JSEncrypt', var.get('JSEncrypt'))
    var.get('exports').put('default', var.get('JSEncrypt'))
    var.get('Object').callprop('defineProperty', var.get('exports'), Js('__esModule'), Js({'value':Js(True)}))
PyJs_anonymous_0_._set_name('anonymous')
@Js
def PyJs_anonymous_280_(PyJsArg_676c6f62616c_, factory, this, arguments, var=var):
    var = Scope({'global':PyJsArg_676c6f62616c_, 'factory':factory, 'this':this, 'arguments':arguments}, var)
    var.registers(['factory', 'global'])
    def PyJs_LONG_281_(var=var):
        return (var.get('factory')(var.get('exports')) if (PyJsStrictEq(var.get('exports',throw=False).typeof(),Js('object')) and PyJsStrictNeq(var.get('module',throw=False).typeof(),Js('undefined'))) else (var.get('define')(Js([Js('exports')]), var.get('factory')) if (PyJsStrictEq(var.get('define',throw=False).typeof(),Js('function')) and var.get('define').get('amd')) else var.get('factory')(var.get('global').put('JSEncrypt', Js({})))))
    PyJs_LONG_281_()
PyJs_anonymous_280_._set_name('anonymous')
PyJs_anonymous_280_(var.get(u"this"), PyJs_anonymous_0_)
pass


# Add lib to the module scope
jsencrypt = var.to_python()