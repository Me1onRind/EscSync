command -nargs=0 PullConfig call s:PullConfig()
command -nargs=0 PushConfig call s:PushConfig()

function! s:PullConfig()
    let filepath = expand("%:p")
    let remoteFileName = s:RemoteFilename(filepath)
    if remoteFileName != ""
        call EscSync#Download(remoteFileName, filepath)
        silent edit!
    endif
endfunction

function! s:PushConfig()
    let filepath = expand("%:p")
    let remoteFileName = s:RemoteFilename(filepath)
    if remoteFileName != ""
        call EscSync#Upload(remoteFileName, filepath)
    endif
endfunction

function! s:RemoteFilename(filepath)
    let filedir = fnamemodify(a:filepath, ":h")
    let files = items(get(g:, "esc_sync_files", {}))
    for file in files
        let tmpKey = expand(file[0])
        if expand(tmpKey) == a:filepath && has_key(file[1], "remote_filename")
                return file[1]["remote_filename"]
        elseif isdirectory(tmpKey) && fnamemodify(tmpKey, ":h") == filedir && has_key(file[1], "remote_prefix")
            return printf("%s:%s", file[1]["remote_prefix"], fnamemodify(a:filepath, ":t"))
        endif
    endfor
    echoerr printf("Not found [%s]'s remote_filename", a:filepath)
    return ""
endfunction
