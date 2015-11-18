// CkOAuth1.h: interface for the CkOAuth1 class.
//
//////////////////////////////////////////////////////////////////////

// This header is generated for Chilkat v9.5.0

#ifndef _CkOAuth1_H
#define _CkOAuth1_H
	
#include "chilkatDefs.h"

#include "CkString.h"
#include "CkMultiByteBase.h"




#if !defined(__sun__) && !defined(__sun)
#pragma pack (push, 8)
#endif
 

// CLASS: CkOAuth1
class CK_VISIBLE_PUBLIC CkOAuth1  : public CkMultiByteBase
{
    private:
	

	// Don't allow assignment or copying these objects.
	CkOAuth1(const CkOAuth1 &);
	CkOAuth1 &operator=(const CkOAuth1 &);

    public:
	CkOAuth1(void);
	virtual ~CkOAuth1(void);

	static CkOAuth1 *createNew(void);
	void CK_VISIBLE_PRIVATE inject(void *impl);

	// May be called when finished with the object to free/dispose of any
	// internal resources held by the object. 
	void dispose(void);

	

	// BEGIN PUBLIC INTERFACE

	// ----------------------
	// Properties
	// ----------------------
	// The authorization header. This is what would be included in the Authorization
	// HTTP request header if it is going to be used as the means for providing the
	// OAuth1 authorization information.
	void get_AuthorizationHeader(CkString &str);
	// The authorization header. This is what would be included in the Authorization
	// HTTP request header if it is going to be used as the means for providing the
	// OAuth1 authorization information.
	const char *authorizationHeader(void);

	// x
	void get_BaseString(CkString &str);
	// x
	const char *baseString(void);

	// The consumer key.
	void get_ConsumerKey(CkString &str);
	// The consumer key.
	const char *consumerKey(void);
	// The consumer key.
	void put_ConsumerKey(const char *newVal);

	// The consumer secret.
	void get_ConsumerSecret(CkString &str);
	// The consumer secret.
	const char *consumerSecret(void);
	// The consumer secret.
	void put_ConsumerSecret(const char *newVal);


	void get_EncodedSignature(CkString &str);

	const char *encodedSignature(void);

	// The URL that includes the OAuth1 query params.
	void get_GeneratedUrl(CkString &str);
	// The URL that includes the OAuth1 query params.
	const char *generatedUrl(void);

	// x
	void get_HmacKey(CkString &str);
	// x
	const char *hmacKey(void);

	// The nonce.
	void get_Nonce(CkString &str);
	// The nonce.
	const char *nonce(void);
	// The nonce.
	void put_Nonce(const char *newVal);

	// The HTTP method, such as "GET", "POST", "PUT", "DELETE", or "HEAD". Defaults to
	// "GET".
	void get_OauthMethod(CkString &str);
	// The HTTP method, such as "GET", "POST", "PUT", "DELETE", or "HEAD". Defaults to
	// "GET".
	const char *oauthMethod(void);
	// The HTTP method, such as "GET", "POST", "PUT", "DELETE", or "HEAD". Defaults to
	// "GET".
	void put_OauthMethod(const char *newVal);

	// The OAuth URL, such as "http://echo.lab.madgex.com/echo.ashx". See
	// http://bettiolo.github.io/oauth-reference-page/ to compare Chilkat results with
	// another tool's results.
	void get_OauthUrl(CkString &str);
	// The OAuth URL, such as "http://echo.lab.madgex.com/echo.ashx". See
	// http://bettiolo.github.io/oauth-reference-page/ to compare Chilkat results with
	// another tool's results.
	const char *oauthUrl(void);
	// The OAuth URL, such as "http://echo.lab.madgex.com/echo.ashx". See
	// http://bettiolo.github.io/oauth-reference-page/ to compare Chilkat results with
	// another tool's results.
	void put_OauthUrl(const char *newVal);

	// The oauth_version. Defaults to "1.0". May be set to the empty string to exclude.
	void get_OauthVersion(CkString &str);
	// The oauth_version. Defaults to "1.0". May be set to the empty string to exclude.
	const char *oauthVersion(void);
	// The oauth_version. Defaults to "1.0". May be set to the empty string to exclude.
	void put_OauthVersion(const char *newVal);

	// x
	void get_QueryString(CkString &str);
	// x
	const char *queryString(void);

	// The generated base64 signature.
	void get_Signature(CkString &str);
	// The generated base64 signature.
	const char *signature(void);

	// The signature method. Defaults to "HMAC-SHA1".
	void get_SignatureMethod(CkString &str);
	// The signature method. Defaults to "HMAC-SHA1".
	const char *signatureMethod(void);
	// The signature method. Defaults to "HMAC-SHA1".
	void put_SignatureMethod(const char *newVal);

	// The timestamp, such as "1441632569".
	void get_Timestamp(CkString &str);
	// The timestamp, such as "1441632569".
	const char *timestamp(void);
	// The timestamp, such as "1441632569".
	void put_Timestamp(const char *newVal);

	// The token.
	void get_Token(CkString &str);
	// The token.
	const char *token(void);
	// The token.
	void put_Token(const char *newVal);

	// The token secret
	void get_TokenSecret(CkString &str);
	// The token secret
	const char *tokenSecret(void);
	// The token secret
	void put_TokenSecret(const char *newVal);



	// ----------------------
	// Methods
	// ----------------------
	// Adds an extra name/value parameter to the OAuth1 signature.
	bool AddParam(const char *name, const char *value);


	// Generate the signature based on the property settings. Input properties are
	// OauthVersion, OauthMethod, Url, ConsumerKey, ConsumerSecret, Token, TokenSecret,
	// Nonce, and Timestamp.
	bool Generate(void);


	// Removes a name/value parameter from the OAuth1 signature.
	bool RemoveParam(const char *name);






	// END PUBLIC INTERFACE


};
#if !defined(__sun__) && !defined(__sun)
#pragma pack (pop)
#endif


	
#endif
