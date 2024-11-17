<script>
  let activeSection = '';
  let showMenu = false;
  let selectedPortal = "Welcome"; // Default text for the home screen

  function toggleMenu() {
    showMenu = !showMenu;
  }

  // Set the active section and close the menu
  function setActiveSection(section) {
    activeSection = section;
    selectedPortal = `${section.charAt(0).toUpperCase() + section.slice(1)} Portal`;
    showMenu = false; // Close the menu after selecting a section
  }

  // Update the welcome message based on the portal selected
  function updatePortal(action) {
    selectedPortal = `${activeSection.charAt(0).toUpperCase() + activeSection.slice(1)} Portal - ${action}`;
  }
</script>

<div>
  <!-- Hamburger/X Menu Icon -->
  <div class="menu-toggle" on:click={toggleMenu}>
    {#if showMenu}
      X
    {:else}
      ☰
    {/if}
  </div>
  <!-- Full Height Sliding Menu -->
  <div class="menu" class:open={showMenu}>
    <div class="menu-section" on:click={() => setActiveSection('users')}>Users</div>
    <div class="menu-section" on:click={() => setActiveSection('institutions')}>Institutions</div>
    <div class="menu-section" on:click={() => setActiveSection('education')}>Education</div>
    <div class="menu-section" on:click={() => setActiveSection('experience')}>Experience</div>
  </div>


  <div class="welcome-message">
    {selectedPortal}
  </div>


  <!-- CRUD Buttons -->
  {#if activeSection}
    <div class="crud-buttons">
      <button
        class="crud-button"
        on:click={() => {
          updatePortal('Create');
          window.location.href = `/${activeSection}/create`;
        }}
      >
        Create
      </button>
      <button
        class="crud-button"
        on:click={() => {
          updatePortal('Read');
          window.location.href = `/${activeSection}/read`;
        }}
      >
        Read
      </button>
      <button
        class="crud-button"
        on:click={() => {
          updatePortal('Delete');
          window.location.href = `/${activeSection}/delete`;
        }}
      >
        Delete
      </button>
      <button
        class="crud-button"
        on:click={() => {
          updatePortal('Update');
          window.location.href = `/${activeSection}/update`;
        }}
      >
        Update
      </button>
    </div>
  {/if}


</div>

<style>
  /* Hamburger/X Menu Toggle Button */
  .menu-toggle {
    font-size: 24px;
    cursor: pointer;
    padding: 10px;
    background-color: #007bff;
    color: white;
    border-radius: 50%;
    position: fixed;
    top: 20px;
    right: 20px;
    z-index: 101;
    text-align: center;
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background-color 0.3s ease;
  }

  .menu-toggle:hover {
    background-color: #0056b3;
  }

  /* Sliding Menu Styles */
  .menu {
    position: fixed;
    top: 0;
    left: -35%;
    height: 100%;
    width: 35%;
    background-color: #f9f9f9;
    border-right: 1px solid #ccc;
    box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
    transition: left 0.3s ease;
    z-index: 100;
  }

  .menu.open {
    left: 0;
  }

  .menu-section {
    padding: 20px;
    font-size: 18px;
    cursor: pointer;
    border-bottom: 1px solid #ccc;
    background-color: #f9f9f9;
    transition: background-color 0.3s ease;
  }

  .menu-section:hover {
    background-color: #e0e0e0;
  }

  .welcome-message {
    position: absolute;
    top: 25%; /* Position 30% from the top */
    left: 50%; /* Center horizontally */
    transform: translateX(-50%); /* Adjust for true horizontal centering */
    font-size: 5rem; /* Font size for readability */
    font-weight: bold;
    color: #555; /* Subtle color */
    z-index: 1; /* Ensure it does not overlap buttons */
    text-align: center;
    animation: fadeIn 1s ease-in-out; /* Optional fade-in animation */
  }

  /* CRUD Buttons in Center */
.crud-buttons {
  display: flex;
  justify-content: center; /* Horizontally center the buttons */
  align-items: center; /* Vertically center the buttons */
  height: 100vh; /* Full screen height */
  width: 100vw; /* Full screen width */
  position: absolute; /* Make sure it covers the whole screen */
  top: 0;
  left: 0;
  background-color: #f9f9f9; /* Optional background to make buttons stand out */
  gap: 30px; 
}

.crud-button {
  width: 120px;
  height: 120px;
  border: none;
  border-radius: 50%; /* Circular shape */
  background: radial-gradient(circle, #0965c7, #0056b3); /* Eye-catching gradient */
  color: white;
  font-size: 18px;
  font-weight: bold;
  cursor: pointer;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Subtle shadow */
  transition: all 0.3s ease-in-out; /* Smooth animation */
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.crud-button:hover {
  transform: scale(1.15); /* Zoom effect on hover */
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3); /* Enhance shadow */
  background: radial-gradient(circle, #3587de, #0056b3); /* Reverse gradient effect */
}

.crud-button:active {
  transform: scale(0.95); /* Slight shrink effect on click */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3); /* Restore shadow */
}

.crud-button:focus {
  outline: none; /* Remove focus outline */
  border: 2px solid #fff; /* Optional focus border */
}

/* Optional fade-in animation for welcome message */
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
</style>
