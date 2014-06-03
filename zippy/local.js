// Note: New keys must be additionally defined in default.js before being overriden here.
module.exports = {
  // Add a non-empty value to the zero-ith key.
  signatureKeys: {0: 'abc'},
  // These are OAuth-related key, secret and realm.
  OAuthCredentials: {
    consumerKey: 'dpf43f3p2l4k3l03',
    consumerSecret: 'kd94hf93k423kf44',
  },
  OAuthRealm: 'Zippy',
  // Session secret cannot be blank.
  sessionSecret: 'tobereplaced',
  logging: {format: 'dev'}
};
