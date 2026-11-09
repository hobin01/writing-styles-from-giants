# Why two DNS resolvers disagree after a record is created

[한국어](strict.ko.md) · [light](light.md) · [standard](standard.md)

[Question and sources](standard.md#question)

### Strict

> NXDOMAIN means the authoritative DNS response said **photos.example.org does not exist** when each resolver looked it up. A negative cache stores that answer temporarily so repeated queries do not have to go back to the authority. Here, each resolver’s cache time is the smaller of 240 and 600 seconds: 240 seconds.
>
> Bay’s timeline: it received NXDOMAIN at 09:10, so that cached answer expires at 09:14. Its 09:15 query comes after expiry; with the updated authority reachable, Bay can look up the name again and get the new A record.
>
> Ridge’s timeline: it received NXDOMAIN at 09:12, so its cached answer expires at 09:16. At 09:15 it can still answer from that cache, so its client can receive NXDOMAIN while Bay’s client gets the A record. Ridge can first pick up the new record on a query at or after 09:16, when the cached answer has expired and Ridge can ask the updated authority.
>
> For a transfer check, keep both lookup times and the record addition fixed, but move Ridge’s next query to 09:16: its old answer is expired then, so it can fetch the A record. The precise time that query arrives is separate; no new query is assumed to occur automatically at expiry.
