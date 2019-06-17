# 패키지 사용자가 echo.py 모듈을 쓸 때 import로
# from pygame.sound import *
# 를 하기 위해서는 원래
# __all__ = ['echo', 'effect' ...]
# 를 해줘야하는데
# from . import echo
# 가 있으면 없어도 작동함

__all__ = ['effect', 'echo']    # import * 했을 때
from . import echo
