# -*- mode: python -*-

block_cipher = None


a = Analysis(['vending_machine.py'],
             pathex=['D:\\2018-2019��ѧ�ڱ���\\python_curriculum\\2-3_�ۺ�ѵ��2_�б�ѵ��'],
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
          name='vending_machine',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
