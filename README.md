# dom-brute

Find domains and 3rd party hosted services with a prefix of a company name.

Prefix of example would generate lists like.

```
example.com
example.org
example.net
```

It will write two files.

`example-domains-200.txt`
`starbucks-domains-non-200.txt`

First one will be everything that has returned a 200 ok after any redirects
Second is one that will return anything but 200 OK but alive hosts.
