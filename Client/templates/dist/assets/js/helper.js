var AUTHENTICATION_TOKEN = null;

function setAuth(data)
{
	console.log(data);
 	AUTHENTICATION_TOKEN = data;
}

function getAuth(data)
{
	return AUTHENTICATION_TOKEN;
}