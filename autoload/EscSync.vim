if has("python")
    let g:esc_sync_py = "python"
elseif has("python3")
    let g:esc_sync_py = "python3"
else
    echoerr "Your vim not support python"
endif

exec g:esc_sync_py "import sys"
exec g:esc_sync_py "cwd = vim.eval('expand(\"<sfile>:p:h\")')"
exec g:esc_sync_py "sys.path.insert(0, cwd)"
exec g:esc_sync_py "from esc_sync.gist import GistApi"
exec g:esc_sync_py "from esc_sync.command import Command"
exec g:esc_sync_py "from esc_sync.logger import setDebugModel"
if get(g:, "esc_sync_debug", 0) == 1
    exec g:esc_sync_py "setDebugModel(True)"
endif

function! EscSync#Download(remoteFilename, localPath)
    let token = get(g:, "esc_sync_github_token", "")
    let gistId = get(g:, "esc_sync_gist_id", "")
    let backup = get(g:, "esc_sync_backup", 0)
    exec g:esc_sync_py printf("api = GistApi(\"%s\",\"%s\",\"%s\")", token, gistId, a:remoteFilename)
    exec g:esc_sync_py printf("Command.download(api, \"%s\", %d)", a:localPath, backup)
endfunction

function! EscSync#Upload(remoteFilename, localPath)
    let token = get(g:, "esc_sync_github_token", "")
    let gistId = get(g:, "esc_sync_gist_id", "")
    exec g:esc_sync_py printf("api = GistApi(\"%s\",\"%s\",\"%s\")", token, gistId, a:remoteFilename)
    exec g:esc_sync_py printf("Command.upload(api, \"%s\")", a:localPath)
endfunction
