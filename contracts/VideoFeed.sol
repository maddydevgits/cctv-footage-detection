// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract VideoFeed {

  string[] _owners;
  string[] _dates;
  string[] _times;
  string[] _videohashes;

  function addVideoHash(string memory owner,string memory date,string memory time,string memory videohash) public {
    _owners.push(owner);
    _dates.push(date);
    _times.push(time);
    _videohashes.push(videohash);
  }

  function viewHashes() public view returns(string[] memory,string[] memory,string[] memory,string[] memory) {
    return(_owners,_dates,_times,_videohashes);
  }
}
