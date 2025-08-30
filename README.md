# PyArmor Isolation Test

This is a repository that is used in order to re-produce the shared runtime issue mentioned in here (https://github.com/dashingsoft/pyarmor/issues/2192#event-19386564379)

This test is using PyArmor 9.1.8


## Pre-requisites

* uv

## Run


```bash
uv sync
```

* Generate the shared runtime

* Clear the dist folder
```bash
rm -rf dist
```

```bash
uv run pyarmor gen runtime -O resources/pyarmor_runtime
```

* Obfuscate the main app;

```bash
uv run pyarmor gen --no-wrap --enable-jit --use-runtime resources/pyarmor_runtime -r main_app/main.py
```

* Obfuscate the side packages;

```bash
uv run pyarmor gen --no-wrap --enable-jit --use-runtime resources/pyarmor_runtime -r side_app
```

* Copy the shared runtime into the `dist` folder

```bash
cp -r resources/pyarmor_runtime/pyarmor_runtime_000000 ./dist/
```

At this point here how the dist folder should look like;

```bash
- dist
    |_ main.py              (obfuscated)
    |_ pyarmor_runtime_000000
    |_ side_app
        |_  __init__.py     (obfuscated)
        |_  sidemodule1.py (obfuscated)
        |_  sidemodule2.py (obfuscated)
```


## Run the obfuscated main app

```bash
cd dist
uv run main.py
```

The output is;

```bash
Traceback (most recent call last):
  File "<frozen __main__>", line 3, in <module>
  File "<frozen main>", line 23, in <module>
  File "<frozen main>", line 13, in main
RuntimeError: protection exception (16777946)
```
