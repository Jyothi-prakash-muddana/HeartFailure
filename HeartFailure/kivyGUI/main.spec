# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2,glew


block_cipher = None


a = Analysis(['main.py'],
             pathex=['E:\\HeartFailure'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

a.datas + [('welcomewindow.kv','E:\\HeartFailure\\welcomewindow.kv','DATA'),
('windowmanager.kv','E:\\HeartFailure\\windowmanager.kv','DATA'),
('widgets.kv','E:\\HeartFailure\\widgets.kv','DATA'),
('formwindow.kv','E:\\HeartFailure\\formwindow.kv','DATA'),
('fileuploadwindow.kv','E:\\HeartFailure\\fileuploadwindow.kv','DATA')
]

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False)

coll = COLLECT(exe,
Tree('E:\\HeartFailure\\'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
