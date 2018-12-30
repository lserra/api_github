% include('header_m.tpl')
        <main role="main" class="col-md-9 ml-sm-auto col-lg-10 pt-3 px-4">
          <!-- Title -->
          <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pb-2 mb-3 border-bottom">
                <h1 class="h2">GitHub Data Analysis</h1>
          </div>
          
          <!-- Metadata details -->
          <div id="card-metadata">
                <div class="card">
                    <div class="card-header">
                         <a class="card-link" data-toggle="collapse" data-parent="#card-metadata" href="#card-element-request">Request Details</a>
                    </div>
                    <div id="card-element-request" class="collapse show">
                        <div class="card-body">
                            <ul>
                                <li class="list-item">
                                    Not Available - (NA)
                                </li>
                            </ul>                            
                        </div>
                    </div>
                </div>
                <div class="card">
                    <div class="card-header">
                         <a class="card-link collapsed" data-toggle="collapse" data-parent="#card-metadata" href="#card-element-table">Table Details</a>
                    </div>
                    <div id="card-element-table" class="collapse">
                        <div class="card-body">
                            <ul>
                                <li class="list-item">
                                    <strong>Name: </strong>repositories
                                </li>
                                <li class="list-item">
                                    <strong>Description: </strong>store all the repositories found in GitHub
                                </li>
                                <li class="list-item">
                                    <strong>Owner: </strong>datafresh
                                </li>
                                <li class="list-item">
                                    <strong>Columns: </strong>[ id, name_, full_name, description, homepage, git_url, 
                                    ssh_url, language_, private, archived, forks_count, open_issues_count, score, 
                                    size_, stargazers_count, watchers_count ]
                                </li>
                                <li class="list-item">
                                    <strong>Constraints: </strong> no constraints
                                </li>
                                <li class="list-item">
                                    <strong>Foreign Keys: </strong> no foreign keys
                                </li>
                                <li class="list-item">
                                    <strong>Indexes: </strong> [ id, name_, language_ ]
                                </li>
                                <li class="list-item">
                                    <strong>Row Count: </strong>{{rows_count}}
                                </li>
                            </ul>                            
                        </div>
                    </div>
                </div>
            </div>
        </main>
      </div>
    </div>
% include('footer.tpl')