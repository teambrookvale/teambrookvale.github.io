---
permalink: /articles/facebook-marketing-api-location-targeting-part-one
boxclassname: black
author: "Mark Szente"
topic: "Development"
title: "Facebook Marketing API: Location targeting – caveats and solutions (part one)"
leadhead: "Using Facebook Marketing API to create a digital marketing software"
leadtext: "Successfully utilizing the Facebook Marketing API for large-scale applications can be a difficult task. This article aims to show you the common pitfalls of location targeting"
date: '2019-07-08 00:00:00'
---

<div class="arttext" style="text-align:justify;" markdown="1">

Facebook’s Graph API is an intuitive, well-designed interface. With powerful tools like the [Graph API Explorer](https://developers.facebook.com/tools/explorer/), it is relatively easy to incorporate into any system, even if no official Facebook library is available for your platform of choice. Once you got the hang of it, it's a great system to work with. Let's say you know the basics; Graph API poses no difficulty, right? Not necessarily. Let’s look into it!

## Breaking changes

Facebook documentations mention two kinds of breaking changes: version deprecation and “breaking changes”. However, there is a third type: unannounced breaking changes.

These changes occur fairly regularly. For example, there is the `search` API endpoint with the parameter `type=adgeolocation` ([https://developers.facebook.com/docs/marketing-api/targeting-search#geo](https://developers.facebook.com/docs/marketing-api/targeting-search#geo)), which we will be exploring thoroughly in this article. Normally, this endpoint – in line with other endpoints and the documentation – returns an empty `data` array when the search yields no results. However, back in March 2019, this behavior abruptly changed:

```json
{
	"data": [
		{
			"key": "<SEARCH QUERY>",
			"category": "no_match"
		}
	]
}
```

As you can see, instead of an empty array, an array with a single object was returned. This had the potential of breaking any app relying on the documented behavior. After some time, this change seems to have been undone, and “no match” is indicated by an empty `data` array once again.

## Gradual changes and out of date documentations

Non-breaking, gradual changes seem to occur regularly, and, unfortunately, documentations don’t always keep up with them. For example, Facebook began reclassifying select ad geo locations of “city” type as “neighborhood” ones. While not a breaking change, it could affect your app’s behavior if, say, you were explicitly using “city” locations. It took official documentations weeks to actually reflect this process.

## Location targeting

Here are a few things you should keep in mind about the aforementioned `search?type=adgeolocation` endpoint and location targeting in general.

- The endpoint (with app access tokens, more about it in the second part) does not return coordinates. So, if you need to display the results on a map, you will need to use an external provider. Be aware that sometimes there are multiple ad geo locations with the same name, region and type. They can represent slightly (or significantly!) geographical physical locations. An external location/map provider might not be able to differentiate between them.

- The query string (parameter `q`) should not contain region, state or country name, only the name of the locality you wish to target. Rather, you should filter locally, optionally using the `country_code` parameter to limit results. [Query string is not guaranteed to support any string format.](https://developers.facebook.com/support/bugs/575786962844919/)

- When using a `custom_audience`, especially with `address_string`, make sure Facebook can geocode the address. The endpoint `act_<AD ACCOUNT ID>/delivery_estimate` can be used to verify this.

- If you keep encountering issues, such as too few locations are returned for your queries, make sure to try it with another access token. One of our apps had an issue with the production access token, while the test access token worked just fine.

## Conculsion
As you can see, location targeting has many caveats, and it is only the tip of the iceberg. Generally speaking, successfully utilising the Facebook Marketing API for large-scale applications can be a difficult task. In the second part of the article, we are going to showcase our best practices and strategies of dealing with the Facebook API. 
If you would rather have a professional team do the heavy lifting for you, or have any questions please feel free to contact Team Brookvale [here](https://teambrookvale.com.au/contact).
</div>
