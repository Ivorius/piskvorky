import piskvorky, pytest, PiskvorkyException

def test_vyhodnot():
    assert piskvorky.vyhodnot('------x-----') == '-'
    assert piskvorky.vyhodnot('---xxo--xxo-') == '-'
    assert piskvorky.vyhodnot('-x-x-x-x-x-o-o-o') == '-'
    assert piskvorky.vyhodnot('-xxx---oo-x') == 'x'
    assert piskvorky.vyhodnot('o-o--xx--ooo') == 'o'
    assert piskvorky.vyhodnot('oxoxoxoxox') == '!'

def test_nove_pole():
    nove_pole = piskvorky.nove_pole(20)
    assert len(nove_pole) == 20

def test_tah():
    pole = piskvorky.nove_pole(20)
    assert pole == '--------------------'
    assert piskvorky.tah(pole, 0, 'x') == 'x-------------------'
    assert piskvorky.tah(pole, 1, 'o') == '-o------------------'
    assert piskvorky.tah(pole, 19, 'x') == '-------------------x'
    assert piskvorky.tah(pole, 18, 'x') == '------------------x-'
    

def test_tah_exception():
    
    with pytest.raises(PiskvorkyException.PiskvorkyException):
        piskvorky.tah('oxoxoxoxoxoxoxoxoxox', 0, 'x')

    with pytest.raises(PiskvorkyException.PiskvorkyException):
        piskvorky.tah('', 0, 'x')

    with pytest.raises(ValueError):
        piskvorky.tah('-', 1, 'x')
        
    with pytest.raises(ValueError):
        piskvorky.tah('---------------', 20, 'x')
        
    with pytest.raises(ValueError):
        piskvorky.tah('-----------------', -1, 'x')


def test_tah_pocitace():
    with pytest.raises(PiskvorkyException.PiskvorkyException):
        piskvorky.tah_pocitace('xoxoxoxoxoxoxo')

    pole = piskvorky.tah_pocitace('xx-------')
    assert  pole.count('o') == 1 

        


