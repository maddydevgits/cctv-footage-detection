// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract CCTVFootage {

  string adminEmail;
  string adminPassword;

  uint[] _pids;
  string[] _pname;
  string[] _pemail;
  string[] _ppassword;

  uint[] _gids;
  string[] _gname;
  string[] _gemail;
  string[] _gpassword;

  mapping(string=>bool) _registeredPrivate;
  mapping(string=>bool) _registeredGovt;

  uint pid;
  uint gid;

  constructor() {
    pid=0;
    gid=0;
    adminEmail="admin@admin.com";
    adminPassword="admin123";
  }

  function viewAdmin() public view returns(string memory,string memory){
    return (adminEmail,adminPassword);
  }

  function addPrivateOfficial(string memory name,string memory email,string memory password) public{

    require(!_registeredPrivate[email]);

    pid+=1;
    _pname.push(name);
    _pemail.push(email);
    _ppassword.push(password);
    _pids.push(pid);

    _registeredPrivate[email]=true;
  } 

  function viewPrivateOfficial() public view returns(uint[] memory,string[] memory,string[] memory,string[] memory){
    return(_pids,_pname,_pemail,_ppassword);
  }

  function addGovernmentOfficial(string memory name,string memory email,string memory password) public {
    require(!_registeredGovt[email]);

    gid+=1;
    _gname.push(name);
    _gemail.push(email);
    _gpassword.push(password);
    _gids.push(pid);

    _registeredGovt[email]=true;
  }

  function viewGovernmentOfficial() public view returns(uint[] memory,string[] memory,string[] memory,string[] memory){
    return(_gids,_gname,_gemail,_gpassword);
  }

}
