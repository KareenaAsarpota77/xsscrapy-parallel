# xsscrapy-parallel
Python tool to automate and parallelize XSS scanning using xsscrapy, with timeout handling and structured result storage.

## Features

* Parallel scanning using thread pools
* Automatic output saving per target
* Graceful timeout handling
* Simple and customizable configuration

## Requirements

* Python 3.x
* xsscrapy (placed inside the xsscrapy directory)

## Installation

* git clone https://github.com/KareenaAsarpota77/xsscrapy-parallel.git
* cd xsscrapy-parallel

## Usage

1. Add target URLs to targets.txt (one per line)

2. Run:
   python scan.py

## Configuration

* MAX_WORKERS: Number of parallel scans
* total_runtime: Total execution time limit

## Disclaimer

This project is intended for educational purposes and authorized security testing only.

The author is not responsible for any misuse or damage caused by this tool. You are responsible for ensuring that you have permission to test any target.

Unauthorized security testing may violate applicable laws.

## License
Copyright (c) 2014, Dan McInerney All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
Neither the name of Dan McInerney nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
