// Given a valid (IPv4) IP address, return a defanged version of that IP address.

// A defanged IP address replaces every period "." with "[.]".

function defangIPaddr(address) {
  let newAddress = address.split(".");
  return newAddress.join("[.]");
}
