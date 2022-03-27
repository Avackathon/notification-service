# SubNav Notification Service

## Quick start

```
poetry install
poetry shell
python main.py
```

The output should look like this:

```
['NodeID-741aqvs6R4iuHDyd1qT1NrFTmsgu78dc4', 'stops validating', '22cwG7XXFk2ZMEAm5b1HwKr66PtrA28Nm3rzSY5VSNLLtoSQQv', 'at', '2023-01-19 07:22:08']
['NodeID-K7Y79oAmBntAcdkyY1CLxCim8QuqcZbBp', 'stops validating', '22cwG7XXFk2ZMEAm5b1HwKr66PtrA28Nm3rzSY5VSNLLtoSQQv', 'at', '2023-01-20 06:55:24']
['NodeID-C3EY6u4v7DDi6YEbYf1wmXdvkEFXYuXNW', 'stops validating', '22cwG7XXFk2ZMEAm5b1HwKr66PtrA28Nm3rzSY5VSNLLtoSQQv', 'at', '2023-01-20 06:56:20']
['NodeID-AiLGeqQfh9gZY3Y8wLMD15tuJtsJHq5Qi', 'stops validating', '22cwG7XXFk2ZMEAm5b1HwKr66PtrA28Nm3rzSY5VSNLLtoSQQv', 'at', '2023-01-20 06:56:59']
['NodeID-3Hd6WQgNFdR7AHaX9uSEtQpgLJF6bLG1Y', 'stops validating', 'j6Lh7WJyFouXMMsPxZpjhj77HmTE5a1D2SEEivrCW6G1jgnWa', 'at', '2023-01-05 20:57:07']
['NodeID-741aqvs6R4iuHDyd1qT1NrFTmsgu78dc4', 'stops validating', '5fiZcfM5RGqP59JKekF6ZsNXfhcFeioDBopeUbH8t8bxokVjw', 'at', '2023-01-19 07:22:08']
['NodeID-K7Y79oAmBntAcdkyY1CLxCim8QuqcZbBp', 'stops validating', '5fiZcfM5RGqP59JKekF6ZsNXfhcFeioDBopeUbH8t8bxokVjw', 'at', '2023-01-20 06:55:24']
['NodeID-C3EY6u4v7DDi6YEbYf1wmXdvkEFXYuXNW', 'stops validating', '5fiZcfM5RGqP59JKekF6ZsNXfhcFeioDBopeUbH8t8bxokVjw', 'at', '2023-01-20 06:56:20']
['NodeID-AiLGeqQfh9gZY3Y8wLMD15tuJtsJHq5Qi', 'stops validating', '5fiZcfM5RGqP59JKekF6ZsNXfhcFeioDBopeUbH8t8bxokVjw', 'at', '2023-01-20 06:56:59']
['NodeID-HTkPf7hwzrLyDDjAZAqMNQh9oF4B9iebY', 'stops validating', '289RgLnY6tygzCKnUwQZu1cuxzqrM9CjRu9nSwfT88UxJyiuv', 'at', '2022-12-08 17:26:22']
['NodeID-PQRNvZxSZi598GNxbH6joNaUPgxaD5Yaa', 'stops validating', '289RgLnY6tygzCKnUwQZu1cuxzqrM9CjRu9nSwfT88UxJyiuv', 'at', '2022-12-08 19:26:22']
['NodeID-HTkPf7hwzrLyDDjAZAqMNQh9oF4B9iebY', 'stops validating', 'UCJGxBvsAcopBAAuBwd9uZ9GdumwRVbCp4Qj2jX6kGJ68121u', 'at', '2022-12-08 17:26:22']
['NodeID-PQRNvZxSZi598GNxbH6joNaUPgxaD5Yaa', 'stops validating', 'UCJGxBvsAcopBAAuBwd9uZ9GdumwRVbCp4Qj2jX6kGJ68121u', 'at', '2022-12-08 19:26:22']
...
```

This is the listing of every nodes validating on Fuji, the subnets they are validating and the end of the leasing period.

## TODO

We could not finish this part of the project but we were hopping to periodically run this script and sent an email notification to both Subnet owner and Node owner if they are registered on [SubNav](https://github.com/Avackathon/subnav).
