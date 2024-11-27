

export const uploadNextChunk = (file) => {
    const { token } = useAuth()
	const config = useRuntimeConfig()

	file.status = 1 // uploading
    var xhr = new XMLHttpRequest();
	xhr.open('POST', `${config.public.baseURL}/rental/file-upload/`, true);
    xhr.setRequestHeader('Authorization', token.value)

    xhr.upload.addEventListener('progress', function(e) {
        if (e.lengthComputable) {
            var totalProgress = ((file.offset + e.loaded) / file.file.size) * 100;
			file.progress = Math.round(totalProgress)
        }
    }, false);

    xhr.onload = function(e) {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            file.id = response.id;
            file.offset = response.offset;

            if (response.status === 'completed') {
				file.status = 2 // upload completed
				file.link = response.file_url
            } else {
                uploadNextChunk(file);
            }
        } else {
			file.status = 3 // upload failed
        }
    };

    var chunk = file.file.slice(file.offset, file.offset + config.public.chunkSize);
    var formData = new FormData();
    formData.append('chunk', chunk);
    formData.append('id', file.id);
    formData.append('filename', file.file.name);
    formData.append('total_size', file.file.size);
    xhr.send(formData);
}

export const dataURLtoFile = (dataurl, filename) => {
    var arr = dataurl.split(','), mime = arr[0].match(/:(.*?);/)[1],
        bstr = atob(arr[1]), n = bstr.length, u8arr = new Uint8Array(n);
    while(n--){
        u8arr[n] = bstr.charCodeAt(n);
    }
    return new File([u8arr], filename, {type:mime});
}

export const getFileType = (filename) => {
    const ext = filename.split('.').pop().toLowerCase()
    if (['mp4', 'webm', 'ogg'].includes(ext)) {
        return 'video'
    } else if (['jpg', 'jpeg', 'png', 'gif'].includes(ext)) {
        return 'image'
    } else {
        return 'unknown'
    }
}