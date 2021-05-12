# mydxf2png
將 dxf 轉檔，輸出 png<br>
<img src="screenshot/95164029.png">
<br>
作者：<br>
  (2020) Hamza Mohamed Abd Al Hakeem<br>
  (2021) Feather Mountain (https://3wa.tw)<br>
License：<br>
  MIT<br>
編譯方法：<br>
<ul>
  <li>1. install miniconda : https://repo.anaconda.com/miniconda/Miniconda3-py39_4.9.2-Windows-x86_64.exe</li>
  <li>2. conda install matplotlib</li>
  <li>3. conda install pyinstaller</li>
  <li>4. conda install ezdxf</li>
  <li>5. conda install wxPython</li>
  <li>6. 執行測試：C:\ProgramData\Miniconda3\python.exe dxf2png.py</li>
  <li>7. 編譯：C:\ProgramData\Miniconda3\scripts\pyinstaller.exe -F dxf2png.py</li>
  <li>8. 成功就會產生 dist\dxf2png.exe</li> 
</ul>
  
使用方法：<br>
  dxf2png.exe source.dxf output.png<br>
  <br>
  例如:<br>
  dxf2png.exe 95164029.dxf 95164029.png<br>
  dxf2png.exe 95181024.dxf 95181024.png<br>
<br>
Reference:<br>
  https://github.com/Hamza442004/DXF2img<br>
