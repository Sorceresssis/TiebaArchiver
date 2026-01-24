# note-tech

## 环境搭建

### 报错

- 使用 uv 虚拟环境，打开 PowerShell 命令行报错。

报错内容

```text
Split-Path : Cannot bind argument to parameter 'Path' because it is null.
At xxxxxxxx\.venv\Scripts\activate.ps1:23 char:31
+ $script:BASE_DIR = Split-Path (Resolve-Path "$THIS_PATH/..") -Parent
+                               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidData: (:) [Split-Path], ParameterBindingValidationException
    + FullyQualifiedErrorId : ParameterArgumentValidationErrorNullNotAllowed,Microsoft.PowerShell.Commands.SplitPathCommand
```

安装下列代码修改 `\.venv\Scripts\activate.ps1` 文件

```powershell [activate.ps1]
# $script:THIS_PATH = $myinvocation.mycommand.path
# $script:BASE_DIR = Split-Path (Resolve-Path "$THIS_PATH/..") -Parent

if ($MyInvocation.MyCommand.Path) {
    $script:THIS_PATH = $MyInvocation.MyCommand.Path
} elseif ($PSCommandPath) {
    $script:THIS_PATH = $PSCommandPath
} else {
    $script:THIS_PATH = (Get-Location).Path
}
```

## 开发

### Pyinstaller

```shell
python -m PyInstaller --onefile --name=TiebaArchiver .\cli_entry.py
```

## protobuff

```powershell
Get-Content -LiteralPath "input" -AsByteStream | protoc --decode_raw > output.txt
```
