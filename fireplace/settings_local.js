define('settings_local', [], function() {
    // Override settings here!
    return {
        api_url: 'http://zamboni.jaredkerim.com',
        api_cdn_whitelist: {
        },
        //media_url: 'http://fireplace.jaredkerim.com/media/'
        media_url: 'https://marketplace-dev-cdn.allizom.org/media/'
    };
});
