#include "Poco/Net/Context.h"
#include "Poco/URI.h"
#include "Poco/Net/HTTPSClientSession.h"

using Poco::Net::Context; 
using Poco::Net::HTTPSClientSession;
using Poco::URI;

int main()
{
   URI uri("https://pocoproject.org/");

   const Context::Ptr context = new Context(Context::CLIENT_USE, "", "", "", Context::VERIFY_NONE, 9, false, "ALL:!ADH:!LOW:!EXP:!MD5:@STRENGTH");

   HTTPSClientSession session(uri.getHost(), uri.getPort(), context);
}
