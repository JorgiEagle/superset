# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from superset.utils.urls import modify_url_query

EXPLORE_CHART_LINK = "http://localhost:9000/explore/?form_data=%7B%22slice_id%22%3A+76%7D&standalone=true&force=false"

EXPLORE_DASHBOARD_LINK = "http://localhost:9000/superset/dashboard/3/?standalone=3"


def test_convert_chart_link() -> None:
    test_url = modify_url_query(EXPLORE_CHART_LINK, standalone="0")
    assert (
        test_url
        == "http://localhost:9000/explore/?form_data=%7B%22slice_id%22%3A%2076%7D&standalone=0&force=false"
    )


def test_convert_dashboard_link() -> None:
    test_url = modify_url_query(EXPLORE_DASHBOARD_LINK, standalone="0")
    assert test_url == "http://localhost:9000/superset/dashboard/3/?standalone=0"


def test_convert_dashboard_link_with_integer() -> None:
    test_url = modify_url_query(EXPLORE_DASHBOARD_LINK, standalone=0)
    assert test_url == "http://localhost:9000/superset/dashboard/3/?standalone=0"


def test_preserves_repeated_query_params() -> None:
    url = "http://localhost:9000/explore/?form_data_key=xyz&filters=a&filters=b"
    test_url = modify_url_query(url, standalone="3")
    assert "filters=a" in test_url
    assert "filters=b" in test_url
    assert "standalone=3" in test_url
    assert "form_data_key=xyz" in test_url


def test_preserves_blank_query_params() -> None:
    url = "http://localhost:9000/x/?empty=&keep=1"
    test_url = modify_url_query(url, standalone="3")
    assert "empty=" in test_url
    assert "keep=1" in test_url
    assert "standalone=3" in test_url


def test_repeated_params_not_collapsed() -> None:
    url = "http://localhost:9000/explore/?a=1&a=2&a=3"
    test_url = modify_url_query(url, standalone="0")
    assert "a=1" in test_url
    assert "a=2" in test_url
    assert "a=3" in test_url
    assert "standalone=0" in test_url
