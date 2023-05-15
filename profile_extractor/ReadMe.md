Requires Source code change:
agents > toolbox > seach_tool > get_profile_url > search.run > gointo run > process_response > for `elif "snippet" in res["organic_results"][0].keys(): ` instead of `snippet` replace it with `link` because the response from SerpApi contains the information on "link"
