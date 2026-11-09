# Why two DNS resolvers disagree after a record is created

[한국어](strict.ko.md) · [light](light.md) · [standard](standard.md) · **strict**

### Question

> Two independent DNS resolvers look up photos.example.org. Bay gets NXDOMAIN at 09:10 and Ridge gets NXDOMAIN at 09:12. Each caches that answer for the smaller of the SOA TTL (240 seconds) and the SOA MINIMUM (600 seconds). At 09:13 the operator adds an A record. Both resolvers receive another query at 09:15. The updated authority is reachable; assume no eviction, early refresh or local override. Why can the two clients get different answers, and when can Ridge first pick up the new record?

**Sources** · [IETF RFC 2308, Negative Caching of DNS Queries](https://www.rfc-editor.org/rfc/rfc2308.html#section-5)

### With the skill

> NXDOMAIN means the authoritative DNS response said **photos.example.org does not exist** when each resolver looked it up. A negative cache stores that answer temporarily so repeated queries do not have to go back to the authority. Here, each resolver’s cache time is the smaller of 240 and 600 seconds: 240 seconds.
>
> Bay’s timeline: it received NXDOMAIN at 09:10, so that cached answer expires at 09:14. Its 09:15 query comes after expiry; with the updated authority reachable, Bay can look up the name again and get the new A record.
>
> Ridge’s timeline: it received NXDOMAIN at 09:12, so its cached answer expires at 09:16. At 09:15 it can still answer from that cache, so its client can receive NXDOMAIN while Bay’s client gets the A record. Ridge can first pick up the new record on a query at or after 09:16, when the cached answer has expired and Ridge can ask the updated authority.
>
> For a transfer check, keep both lookup times and the record addition fixed, but move Ridge’s next query to 09:16: its old answer is expired then, so it can fetch the A record. The precise time that query arrives is separate; no new query is assumed to occur automatically at expiry.

### Without the skill

> The negative-cache lifetime is the smaller of the SOA TTL and SOA MINIMUM: **240 seconds**. Bay’s NXDOMAIN cache expires at **09:14**; Ridge’s expires at **09:16**.
>
> So at 09:15, Bay can query the updated authority and get the new A record, while Ridge can still answer from its cached NXDOMAIN. Ridge can first pick up the new record at **09:16**, when its negative cache expires.
