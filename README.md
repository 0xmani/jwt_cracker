# jwt_cracker

Simple HS256 JWT token brute force cracker.

Effective only to crack JWT tokens with weak secrets. Recommendation: Use strong long secrets or RS256 tokens.

Usage
From command line:

ruby jwt-cracker.rb <token> <wordlist>
