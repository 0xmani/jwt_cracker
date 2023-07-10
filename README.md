# jwt_cracker

Simple HS256 JWT token brute force cracker.

Effective only to crack JWT tokens with weak secrets. 
* **Recommendation**: Use strong long secrets or RS256 tokens.

## Usage

From command line:
python3 jwt_cracker.py <token> <wordlist>

## Where:

* **token:** the full HS256 JWT token string to crack
* **wordlist:** path to wordlist

## Example
  
Cracking the default [jwt.io example](https://jwt.io):

```bash
python jwt_cracker.py"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ" ~/opt/worlist.txt
```
