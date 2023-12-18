# Define user details
$firstName = "Franz"
$lastName = "Ferdinand"
$username = "ferdi"
$department = "TPS"
$office = "Springfield"
$email = "ferdi@GlobeXpower.com"

# Define organizational unit (OU) path where the user will be created
$ouPath = "OU=Users,DC=corp,DC=globexpower,DC=com"

# Generate user principal name (UPN)
$upn = "$username@$($env:USERDNSDOMAIN)"

# Set the password for the new user
$password = "P@ssw0rd"  # Change this to a secure password

# Import the Active Directory module
Import-Module ActiveDirectory

# Create the new user
New-ADUser -SamAccountName $username -UserPrincipalName $upn -GivenName $firstName -Surname $lastName -Department $department -Office $office -EmailAddress $email -Enabled $true -AccountPassword (ConvertTo-SecureString -AsPlainText $password -Force) -Path $ouPath

# Display a message indicating success
Write-Host "User $username created successfully."
