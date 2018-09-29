# -*- mode: python -*-

block_cipher = None


a = Analysis(['shopping_list.py'],
             pathex=['D:\\2018-2019上学期备课\\python_curriculum\\2-3_综合训练2_列表训练'],
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
          name='shopping_list',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
