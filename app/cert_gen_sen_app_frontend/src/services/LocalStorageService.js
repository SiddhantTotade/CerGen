const storeToken = (value) => {
    if (value) {
        const { access, refresh } = value
        localStorage.setItem('access_token', access)
        localStorage.setItem('refresh_token', refresh)
    }
}

const getToken = () => {
    let access_token = localStorage.getItem('access_token')
    let refresh_token = localStorage.getItem('refresh_token')

    return { access_token, refresh_token }
}

const removeToken = () => {
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
}

export { storeToken, getToken, removeToken }