<script>
  import { onMount } from 'svelte';
  let activeSection = '';

  function setActiveSection(section) {
    activeSection = section;
  }
</script>



<div>
  <div class="section" on:click={() => setActiveSection('users')} class:active={activeSection === 'users'}>
  Users
  </div>
  <div class="crud-options" class:active={activeSection === 'users'}>
  <a href="users/create">Create User</a>
  <a href="users/delete">Delete User</a>
  <a href="users/read">Read User</a>
  <a href="users/[userId]/update">Update User</a>
  </div>

  <div class="section" on:click={() => setActiveSection('institutions')} class:active={activeSection === 'institutions'}>
  Institutions
  </div>
  <div class="crud-options" class:active={activeSection === 'institutions'}>
  <a href="institutions/create">Create Institution</a>
  <a href="institutions/delete">Delete Institution</a>
  <a href="institutions/read">Read Institution</a>
  <a href="institutions/[institutionId]/update">Update Institution</a>
  </div>

  <div class="section" on:click={() => setActiveSection('education')} class:active={activeSection === 'education'}>
  Education
  </div>
  <div class="crud-options" class:active={activeSection === 'education'}>
  <a href="education/create">Create Education</a>
  <a href="education/delete">Delete Education</a>
  <a href="education/read">Read Education</a>
  <a href="education/[educationId]/update">Update Education</a>
  </div>
<div class="section" on:click={() => setActiveSection('experience')} class:active={activeSection === 'experience'}>
  Experience
</div>
<div class="crud-options" class:active={activeSection === 'experience'}>
  <a href="experience/create">Create Experience</a>
  <a href="experience/delete">Delete Experience</a>
  <a href="experience/read">Read Experience</a>
  <a href="experience/[experienceId]/update">Update Experience</a>
</div>
</div>
<style>
  .section {
    padding: 10px;
    margin: 5px;
    cursor: pointer;
    border: 1px solid #ccc;
    border-radius: 4px;
    background-color: #f9f9f9;
    transition: background-color 0.3s ease;
  }

  .section:hover {
    background-color: #e0e0e0;
  }

  .section.active {
    background-color: #007bff;
    color: white;
  }

  .crud-options {
    display: none;
    margin-left: 20px;
  }

  .crud-options.active {
    display: block;
  }

  .crud-options a {
    display: block;
    margin: 5px 0;
    color: #007bff;
    text-decoration: none;
  }

  .crud-options a:hover {
    text-decoration: underline;
  }
</style>