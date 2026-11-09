# Why two DNS resolvers disagree after a record is created

[한국어](light.ko.md) · **light** · [standard](standard.md) · [strict](strict.md)

### Question

> Two independent DNS resolvers look up photos.example.org. Bay gets NXDOMAIN at 09:10 and Ridge gets NXDOMAIN at 09:12. Each caches that answer for the smaller of the SOA TTL (240 seconds) and the SOA MINIMUM (600 seconds). At 09:13 the operator adds an A record. Both resolvers receive another query at 09:15. The updated authority is reachable; assume no eviction, early refresh or local override. Why can the two clients get different answers, and when can Ridge first pick up the new record?

**Sources** · [IETF RFC 2308, Negative Caching of DNS Queries](https://www.rfc-editor.org/rfc/rfc2308.html#section-5)

### With the skill

> Bay cached **NXDOMAIN**, meaning the name `photos.example.org` did not exist, at 09:10. Its negative-cache lifetime is the smaller of 240 and 600 seconds: 240 seconds, so that answer expires at 09:14. Ridge cached the same answer at 09:12; its 240-second lifetime expires at 09:16.
>
> The operator adds the A record at 09:13, but that does not change either resolver’s cached answer. At 09:15, Bay’s negative entry has expired, so it can query the reachable authority and return the new record. Ridge’s entry is still valid until 09:16, so it can still return NXDOMAIN. Ridge can first pick up the new record at or after 09:16, when its cached negative answer expires and a query can reach the authority.

### Without the skill

> The negative-cache lifetime is the smaller of the SOA TTL and SOA MINIMUM: **240 seconds**. Bay’s NXDOMAIN cache expires at **09:14**; Ridge’s expires at **09:16**.
>
> So at 09:15, Bay can query the updated authority and get the new A record, while Ridge can still answer from its cached NXDOMAIN. Ridge can first pick up the new record at **09:16**, when its negative cache expires.
