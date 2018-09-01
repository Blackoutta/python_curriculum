# -*- mode: python -*-

block_cipher = None


a = Analysis(['dungeon_game.py'],
             pathex=['E:\\备课\\2018-2019上学期备课\\1-1. 课程简介\\dungeon_v1_cn_exe'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='dungeon_game',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
