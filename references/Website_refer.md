# 1. Theorem

## 1.1 [How to Make Chord Correct](http://www.pamelazave.com/chord.html)

The Chord distributed hash table (DHT) is well-known and often used to implement peer-to-peer systems. Chord peers find other peers, and access their data, through a ring-shaped pointer structure in a large identifier space. Despite claims of proven correctness, i.e., eventual reachability, ["Using lightweight modeling to understand Chord"](http://www.pamelazave.com/chord-ccr.pdf) (Pamela Zave; *ACM SIGCOMM Computer Communication Review*, 42(2):50-57, April 2012) has shown that the Chord ring-maintenance protocol is not correct under its original operating assumptions. Not one of the seven claimed invariants is actually an invariant.

Until recently it was not known whether Chord could be made correct under the same operating assumptions, and with the same efficiency. A correct and efficient version of Chord is presented in ["Reasoning about identifier spaces: How to make Chord correct"](http://www.pamelazave.com/TSE_Chord_final.pdf) (Pamela Zave; *IEEE Transactions on Software Engineering,* 43(12):1144-1156, December 2017, DOI 10.1109/TSE.2017.2655056). See erratum below. The contributions of the paper include:

- It provides the first specification of correct operations and initialization for Chord.
- It presents an inductive invariant that is necessary and sufficient to support a proof of correctness. The inductive invariant is surprising because it is extremely simple and does not resemble any of the desired properties of a Chord network.
- It describes two independent proofs of correctness. One proof (given in the paper) is informal and intuitive, and applies to networks of any size. The other proof is based on a formal model in Alloy, and uses fully automated analysis to prove the assertions for networks of bounded size. [The Alloy model of the correct version](http://www.pamelazave.com/correctChord.als) includes properties and proof steps. The two proofs complement each other in several important ways.

Here is a [talk about how to make and prove Chord correct](http://www.pamelazave.com/aFinalChord.pdf). 

["Experiences with protocol description"](http://www.pamelazave.com/wripe.pdf) (Pamela Zave; *1st International Workshop on Rigorous Protocol Engineering,* Vancouver, Canada, October 2011) explains the pitfalls of designing and documenting protocols without the use of modeling tools. The examples used are Chord and SIP (the IETF Session Initiation Protocol).

This work has also led to ["A practical comparison of Alloy and Spin"](http://www.pamelazave.com/compare.pdf) (Pamela Zave; *Formal Aspects of Computing* 27: 239-253, 2015).

For those interested in the comparison, [chordfull.als](http://www.pamelazave.com/chordfull.als) is the Alloy model of the original Chord protocol. A Promela model (for the Spin model-checker) of a version similar to the original, but with some bugs fixed, is in[chordbestccr.pml](http://www.pamelazave.com/chordbestccr.pml) and [chordbestccr.c](http://www.pamelazave.com/chordbestccr.c), with execution instructions in [spindocu.txt](http://www.pamelazave.com/spindocu.txt).

#### Erratum

In ["Reasoning about identifier spaces: How to make Chord correct"](http://www.pamelazave.com/TSE_Chord_final.pdf), Section VI-B, the proof that *Invariant* implies *OrderedSuccessorLists* should read as follows, after the first two paragraphs:

From the picture, the ESL segment *[x, ..., y, ..., z]* must include *r* + 1 principal nodes. If it did not, some principal nodes would be skipped, or there would not be sufficient principals.

*x* cannot be a principal node, because from *NoDuplicates* it cannot be duplicated in the segment *[y, ..., z]*, so it is skipped by that segment. From similar reasoning, *z* cannot be a principal node. 

Consequently the length of *[x, ..., y, ..., z]* is at least *r* + 3. But the length of an entire ESL is *r* + 1, which yields a contradiction.