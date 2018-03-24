### Activate Virtual Environments Indpendent In Each Folder ###

## Setting up Modules and Virtual Environemnt in Each Project Folder ##

``` cd /THORMessageClient ```

``` virtualenv env ```

``` source env/bin/activate ```

``` pip install requests ```

``` pip install Crypto ```

``` pip freeze > requirements.txt ```

``` cd .. ```

``` cd /THORMessageServer ```

``` virtualenv env ```

``` source env/bin/activate ```

``` pip install requests ```

``` pip install Crypto ```

``` pip freeze > requirements.txt ```

``` cd .. ```

``` cd /THORProxyWebServer ```

``` virtualenv env ```

``` source env/bin/activate ```

``` pip install requests ```

``` pip install Crypto ```

``` pip freeze > requirements.txt ```
