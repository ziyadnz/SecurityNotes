### 1. **[PHPStan](https://github.com/phpstan/phpstan.git)**
The PHPStan is a static code analyser and you can analyse your code as online.
**[Try out PHPStan on the on-line playground! »](https://phpstan.org/)**

It's source code is here https://github.com/phpstan/phpstan.git



### 2.  **[local-php-security-checker](https://github.com/fabpot/local-php-security-checker.git)** 
First you need to make it executable 
```c
chmod +x local-php-security-checker_1.2.0_linux_amd64
```

You can copy this in the php project folder. (Which contains composer folder)

From a directory containing a PHP project that uses Composer, check for known
vulnerabilities by running the binary without arguments or flags:

    $ local-php-security-checker

You can also pass a `--path` to check a specific directory:

    $ local-php-security-checker --path=/path/to/php/project
    $ local-php-security-checker --path=/path/to/php/project/composer.lock


