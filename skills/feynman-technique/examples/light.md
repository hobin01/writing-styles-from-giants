# Why two DNS resolvers disagree after a record is created

[한국어](light.ko.md) · [standard](standard.md) · [strict](strict.md)

[Question and sources](standard.md#question)

### Light

> Bay cached **NXDOMAIN**, meaning the name `photos.example.org` did not exist, at 09:10. Its negative-cache lifetime is the smaller of 240 and 600 seconds: 240 seconds, so that answer expires at 09:14. Ridge cached the same answer at 09:12; its 240-second lifetime expires at 09:16.
>
> The operator adds the A record at 09:13, but that does not change either resolver’s cached answer. At 09:15, Bay’s negative entry has expired, so it can query the reachable authority and return the new record. Ridge’s entry is still valid until 09:16, so it can still return NXDOMAIN. Ridge can first pick up the new record at or after 09:16, when its cached negative answer expires and a query can reach the authority.
