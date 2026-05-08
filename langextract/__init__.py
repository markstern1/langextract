# Copyright 2024 LangExtract Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""LangExtract: A library for extracting structured information from text using LLMs.

This is a fork of google/langextract with additional features and improvements.

Basic usage:
    >>> import langextract
    >>> result = langextract.extract(text="Paris is the capital of France.", schema={"city": str, "country": str})

Notes (personal fork):
    - See https://github.com/google/langextract for the upstream project.
    - Use `langextract.__version__` to check the current version.
    - The `extract` function is the main entry point for all extraction tasks.
"""

from langextract.core import extract
from langextract.version import __version__

__all__ = [
    "extract",
    "__version__",
]
