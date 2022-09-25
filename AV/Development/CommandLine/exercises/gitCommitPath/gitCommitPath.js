import {
  awardCredit,
  initializeGitExercise,
} from "../../common/commandLineExercise.js";

/*global alert: true, ODSA, console */
$(document).ready(function () {
  const handleAwardCredit =
    (
      getLocalCurrDir,
      getLocalHomeDir,
      getLocalInitialCommit,
      getLocalCurrBranch,
      getRemoteHomeDir,
      getRemoteInitialCommit,
      getRemoteCurrBranch
    ) =>
    (args) => {
      if (args.length > 0 && args[0] === "status") {
        const readme = getLocalHomeDir().find("README");
        const gitignore = getLocalHomeDir().find(".gitignore");
        if (
          readme &&
          readme.isUnchanged() &&
          gitignore &&
          !gitignore.isUnchanged()
        ) {
          const src = getLocalHomeDir().findDeep("src");
          if (src) {
            const app = src.find("app.js");
            const test = src.findWithDeleted("test.js");
            const index = src.find("index.html");
            if (
              app &&
              app.isUnchanged() &&
              test &&
              test.length > 0 &&
              !test[0].isUnchanged() &&
              index &&
              !index.isUnchanged()
            ) {
              awardCredit();
            }
          }
        }
      }
    };

  initializeGitExercise(
    {
      commandTitle: "git commit (path) -m (message)",
      commandDescription:
        "The git commit command with one or more (path) arguments creates a commit containing only the changes to the files or directories at the location or locations specified by (path).",
      challengeDescription:
        'Create a commit containing only the changes to "app.js" and "README". Then, run git status to check that only those changes have been committed.',
    },
    handleAwardCredit,
    "git",
    null,
    null,
    [
      "cd src",
      "rm test.js",
      "vi index.html",
      "touch app.js",
      "git add .",
      "vi ../README ../.gitignore",
    ]
  );
});
