% include('header_i.tpl')       
        <main role="main" class="col-md-9 ml-sm-auto col-lg-10 pt-3 px-4">
            <!-- Title -->
            <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pb-2 mb-3 border-bottom">
                  <h1 class="h2">GitHub Data Analysis</h1>
            </div>

            %if type_msg is not None:
            <!-- Message -->
            <div class="alert alert-{{ class_msg }}" role="alert">
                <strong>{{ type_msg }}: </strong>{{ msg }}
            </div>
            %end

            <!-- Searching repositories -->
            <form action="/search" method="POST">
              <div class="form-group row">
                <div class="col-sm-8">
                  <div class="input-group mb-2 mr-sm-2">
                    <div class="input-group-prepend">
                      <div class="input-group-text">Keyword</div>
                    </div>
                    <input name="keyword" type="text" class="form-control" placeholder="airflow" required="">
                  </div>
                </div>
                <div class="col-sm-4">
                  <button name="search" type="submit" class="btn btn-outline-dark" value="search">
                    Search
                  </button>
                </div>
              </div>
            </form>
            
            <br>

            %if items is not None:
            <h5>Has been found {{ num_repos }} repositories</h5>
            
            <!-- List of repositories has been found -->
            <div class="table-responsive">
              <table class="table table-striped table-sm">
                <thead>
                  <tr>
                    <th>Id</th>
                    <th>Name</th>
                    <th>Homepage</th>
                    <th>Git URL</th>
                    <th>Language</th>
                  </tr>
                </thead>
                <tbody>
                %for item in items:
                  <tr>
                    <td>{{ item.id }}</td>
                    <td>{{ item.name }}</td>
                    <td>{{ item.homepage }}</td>
                    <td>{{ item.git_url }}</td>
                    <td>{{ item.language }}</td>
                  </tr>
                %end
                </tbody>
              </table>            
            %end
        </main>
      </div>
    </div>
% include('footer.tpl')